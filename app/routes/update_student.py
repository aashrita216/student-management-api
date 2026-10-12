from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas
from app.database import get_db

router = APIRouter(tags=["students"])

@router.put("/students/{student_id}", response_model=schemas.StudentResponse)
def update_student(student_id: int, updated_student: schemas.StudentCreate, db: Session = Depends(get_db)):
    student_query = db.query(models.Student).filter(models.Student.id == student_id)
    student = student_query.first()
    
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
        
    student_query.update(updated_student.dict(), synchronize_session=False)
    db.commit()
    return student_query.first()