from fastapi import FastAPI, UploadFile, File
from PyPDF2 import PdfReader
import docx

app = FastAPI(title="AI Resume Analyzer - ML Service")

@app.get("/")
def read_root():
    return {"message": "ML Service is running 🚀"}

@app.post("/upload-resume/")
async def upload_resume(file: UploadFile = File(...)):
    text = ""

    if file.filename.endswith(".pdf"):
        reader = PdfReader(file.file)
        for page in reader.pages:
            text += page.extract_text() + "\n"

    elif file.filename.endswith(".docx"):
        doc = docx.Document(file.file)
        for para in doc.paragraphs:
            text += para.text + "\n"

    else:
        return {"error": "Only PDF and DOCX files are supported"}

    return {
        "filename": file.filename,
        "content_preview": text[:500]  # first 500 characters
    }
