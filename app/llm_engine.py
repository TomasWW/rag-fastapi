import os
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage

# Load API key from environment (Railway)
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

OPENROUTER_API_BASE = "https://openrouter.ai/api/v1"

# Initialize LLM
llm = ChatOpenAI(
    model="mistralai/mistral-7b-instruct",
    temperature=0.7,
    openai_api_base=OPENROUTER_API_BASE
)

def ask_llm(context: str, question: str):
    """Ask the LLM using a provided context."""
    response = llm.invoke([
        HumanMessage(content=f"Using this context:\n{context}\nAnswer the question: {question}")
    ])
    return response.content