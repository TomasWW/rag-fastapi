from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage
import os

llm = ChatOpenAI(
    model="mistralai/mistral-7b-instruct",
    temperature=0.7,
    openai_api_base=os.environ.get("OPENROUTER_API_BASE")
)

def ask_llm(context: str, user_input: str) -> str:
    response = llm.invoke([
        HumanMessage(content=f"Using the following context:\n{context}\n\nAnswer the question: {user_input}")
    ])
    return response.content