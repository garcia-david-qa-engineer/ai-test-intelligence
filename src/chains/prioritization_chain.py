from langchain.prompts import ChatPromptTemplate
from langchain.schema import StrOutputParser
from models.llm_client import get_llm

def build_prioritization_chain():
    """
    Classifies scenarios by test priority.
    """
    prompt = ChatPromptTemplate.from_template("""
You are a QA Release Manager.

Classify the following test scenarios into three groups:
- SMOKE (critical for release)
- REGRESSION (repeat each sprint)
- NIGHTLY (extended coverage, non-blocking)

Explain briefly why each scenario belongs in that group.

Scenarios:
----------------
{gherkin}
----------------

Return Markdown text with group headings and explanations.
""")

    llm = get_llm()
    chain = prompt | llm | StrOutputParser()
    return chain
