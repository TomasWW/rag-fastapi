from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse

app = FastAPI(title="RAG + LLM Demo")


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