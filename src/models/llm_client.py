import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

def get_llm():
    """
    Centralized LLM configuration.
    Easily replaceable with another provider (Azure, Mistral, etc.).
    """
    model_name = os.getenv("MODEL_NAME", "gpt-4o-mini")
    temperature = 0.2  # low temperature for deterministic test design
    return ChatOpenAI(
        model=model_name,
        temperature=temperature,
        api_key=os.getenv("OPENAI_API_KEY"),
    )
