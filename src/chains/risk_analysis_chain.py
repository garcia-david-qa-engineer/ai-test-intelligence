from langchain.prompts import ChatPromptTemplate
from langchain.schema import StrOutputParser
from models.llm_client import get_llm
from utils.helpers import to_json_risk

def build_risk_analysis_chain():
    """
    Analyze potential risks related to the feature.
    Output a JSON risk matrix.
    """
    prompt = ChatPromptTemplate.from_template("""
You are a QA Risk Manager.

From the following requirements, build a risk matrix with:
- category: business / security / UX / compliance / stability
- description
- probability: Low | Medium | High
- severity: Low | Medium | High
- qa_focus: recommendation for QA focus area

Requirements:
{requirements}

Return STRICTLY valid JSON with the following structure:

{{
  "risks": [
    {{
      "category": "security",
      "description": "What could go wrong",
      "probability": "High",
      "severity": "High",
      "qa_focus": "What QA must absolutely validate"
    }}
  ]
}}
""")

    llm = get_llm()
    chain = prompt | llm | StrOutputParser() | to_json_risk
    return chain
