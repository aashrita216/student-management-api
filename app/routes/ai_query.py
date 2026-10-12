from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db

# 🚨 THIS LINE DECLARES THE ROUTER CONTEXT:
router = APIRouter(tags=["AI Query"])

@router.post("/ai/query")
def ask_ai_about_students(prompt: str, db: Session = Depends(get_db)):
    # This endpoint will connect to your Ollama LLM model later
    return {"message": "AI Query endpoint initialized successfully!", "your_prompt": prompt}