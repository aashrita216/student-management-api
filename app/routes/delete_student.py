from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app import models
from app.database import get_db

# 🚨 THIS IS THE CRITICAL LINE THAT WAS MISSING:
router = APIRouter(tags=["students"])

@router.delete("/students/{student_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_student(student_id: int, db: Session = Depends(get_db)):
    student_query = db.query(models.Student).filter(models.Student.id == student_id)
    existing_student = student_query.first()
    
    if not existing_student:
        raise HTTPException(status_code=404, detail="Student not found")
        
    student_query.delete(synchronize_session=False)
    db.commit()
    return None