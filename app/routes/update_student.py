
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas
from app.database import get_db

router = APIRouter(tags=["students"])


@router.put("/students/{student_id}", response_model=schemas.StudentResponse)
def update_student(
    student_id: int,
    updated_student: schemas.StudentCreate,
    db: Session = Depends(get_db)
):
    student = db.query(models.Student).filter(
        models.Student.id == student_id
    ).first()

    if not student:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    student.name = updated_student.name
    student.dob = updated_student.dob
    student.email = updated_student.email
    student.phone = updated_student.phone
    student.course = updated_student.course
    student.address = updated_student.address

    db.commit()
    db.refresh(student)

    return student

