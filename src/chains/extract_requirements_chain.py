from langchain.prompts import ChatPromptTemplate
from langchain.schema import StrOutputParser
from models.llm_client import get_llm
from utils.helpers import clean_markdown

def build_extract_requirements_chain():
    """
    Takes a raw user story (Jira-style or Markdown)
    → returns a list of clear, testable requirements.
    """
    prompt = ChatPromptTemplate.from_template("""
You are a Senior QA Engineer.

Your task is to read a user story and extract all **testable requirements**.

1. Summarize the business objective.
2. List all functional requirements as bullet points.
3. Identify implicit business rules (security, validation, edge cases).

User Story:
----------------
{story}
----------------

Output in Markdown format.
""")

    llm = get_llm()
    chain = prompt | llm | StrOutputParser() | clean_markdown
    return chain
