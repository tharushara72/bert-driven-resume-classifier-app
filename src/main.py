from fastapi import FastAPI, UploadFile, File
from src.processor import extract_text_from_pdf
from src.model_utils import calculate_similarity
import os

app = FastAPI()

@app.post("/score")
async def score_resume(job_description: str, file: UploadFile = File(...)):
    # Save file temporarily
    temp_path = f"temp_{file.filename}"
    with open(temp_path, "wb") as buffer:
        buffer.write(await file.read())
    
    # Process
    resume_text = extract_text_from_pdf(temp_path)
    score = calculate_similarity(resume_text, job_description)
    
    # Cleanup
    os.remove(temp_path)
    
    return {"filename": file.filename, "match_score": f"{score}%"}