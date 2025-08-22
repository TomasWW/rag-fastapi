from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# Import from your internal utils
from app.utils.functions import get_context
from app.llm_engine import ask_llm
from app.rag_engine import qdrant
origins = [
    "http://localhost:5173",  # si probás localmente
]
app = FastAPI(title="RAG + LLM Demo")


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"message": "Hello! This is the RAG + LLM demo API."}


@app.post("/upload_pdf/")
async def upload_pdf(file: UploadFile = File(...)):
    # Save uploaded PDF
    content = await file.read()
    file_location = f"uploads/{file.filename}"
    with open(file_location, "wb") as f:
        f.write(content)
    
    return JSONResponse(content={"filename": file.filename, "status": "uploaded"})

class Message(BaseModel):
    user_input: str


@app.post("/chat/")
async def chat_endpoint(message: Message):
    user_text = message.user_input
    context = get_context(user_text, qdrant)
    bot_response = ask_llm(context, user_text)
    return {"response": bot_response}