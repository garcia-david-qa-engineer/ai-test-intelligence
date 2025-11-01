from langchain.prompts import ChatPromptTemplate
from langchain.schema import StrOutputParser
from models.llm_client import get_llm

def build_test_generation_chain():
    """
    Generates Gherkin test scenarios (Given/When/Then)
    based on requirements and identified risks.
    """
    prompt = ChatPromptTemplate.from_template("""
You are an experienced SDET.

Generate Gherkin-style test scenarios that cover both:
- nominal functional paths
- critical error or risk-based paths

Requirements:
{requirements}

Critical Risks (JSON describing high-severity / high-probability issues):
{risks}

Rules:
- Use standard Gherkin syntax.
- Each scenario must start with 'Scenario:'.
- Cover both success and failure / abuse / security flows.
- Output only valid `.feature` text, nothing else.
""")

    llm = get_llm()
    chain = prompt | llm | StrOutputParser()
    return chain
