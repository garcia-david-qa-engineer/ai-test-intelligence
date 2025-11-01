import argparse
from pathlib import Path
import json

from chains.extract_requirements_chain import build_extract_requirements_chain
from chains.risk_analysis_chain import build_risk_analysis_chain
from chains.test_generation_chain import build_test_generation_chain
from chains.prioritization_chain import build_prioritization_chain

OUTPUT_DIR = Path(__file__).parent / "output"

def read_story(path: Path) -> str:
    return path.read_text(encoding="utf-8")

def write_file(path: Path, content: str):
    path.write_text(content, encoding="utf-8")

def write_json(path: Path, content: dict):
    path.write_text(json.dumps(content, indent=2, ensure_ascii=False), encoding="utf-8")

def main(input_path: str):
    story_path = Path(input_path)
    story_text = read_story(story_path)

    # Step 1: Requirements
    extract_chain = build_extract_requirements_chain()
    requirements_md = extract_chain.invoke({"story": story_text})
    write_file(OUTPUT_DIR / "generated_requirements.md", requirements_md)

    # Step 2: Risk Analysis
    risk_chain = build_risk_analysis_chain()
    risks_json = risk_chain.invoke({"requirements": requirements_md})
    write_json(OUTPUT_DIR / "risk_matrix.json", risks_json)

    # Step 3: Test Generation
    test_chain = build_test_generation_chain()
    gherkin = test_chain.invoke({
        "requirements": requirements_md,
        "risks": risks_json
    })
    write_file(OUTPUT_DIR / "generated_tests.feature", gherkin)

    # Step 4: Prioritization
    prio_chain = build_prioritization_chain()
    priority_plan = prio_chain.invoke({"gherkin": gherkin})
    write_file(OUTPUT_DIR / "priority_plan.md", priority_plan)

    print("✅ Test plan successfully generated! Check the 'output/' directory.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Path to the user story file (.md)")
    args = parser.parse_args()
    main(args.input)
