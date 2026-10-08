from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

import models
import schemas
from database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Student Management API")

@app.get("/")
def home():
    return {"message": "API is running. Access /docs for Swagger UI."}

@app.post("/students", response_model=schemas.StudentResponse, status_code=status.HTTP_201_CREATED)
def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    existing_student = db.query(models.Student).filter(models.Student.email == student.email).first()
    if existing_student:
        raise HTTPException(status_code=400, detail="Student with this email already exists")

    db_student = models.Student(**student.model_dump())
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

@app.get("/students", response_model=List[schemas.StudentResponse])
def get_all_students(db: Session = Depends(get_db)):
    return db.query(models.Student).all()

@app.get("/students/{student_id}", response_model=schemas.StudentResponse)
def get_student_by_id(student_id: int, db: Session = Depends(get_db)):
    student = db.query(models.Student).filter(models.Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

@app.put("/students/{student_id}", response_model=schemas.StudentResponse)
def update_student(student_id: int, student_data: schemas.StudentUpdate, db: Session = Depends(get_db)):
    student_query = db.query(models.Student).filter(models.Student.id == student_id)
    existing_student = student_query.first()

    if not existing_student:
        raise HTTPException(status_code=404, detail="Student not found")

    update_data = student_data.model_dump(exclude_unset=True)
    student_query.update(update_data, synchronize_session=False)
    db.commit()
    db.refresh(existing_student)
    return existing_student

@app.delete("/students/{student_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_student(student_id: int, db: Session = Depends(get_db)):
    student_query = db.query(models.Student).filter(models.Student.id == student_id)
    existing_student = student_query.first()

    if not existing_student:
        raise HTTPException(status_code=404, detail="Student not found")

    student_query.delete(synchronize_session=False)
    db.commit()
    return None