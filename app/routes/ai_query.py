
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app import models

router = APIRouter(tags=["AI Query"])


@router.post("/ai/query")
def ask_ai_about_students(
    prompt: str,
    db: Session = Depends(get_db)
):
    question = prompt.strip().lower()

    if not question:
        raise HTTPException(
            status_code=400,
            detail="Please enter a question."
        )

    # Retrieve student records from the database
    students = db.query(models.Student).all()
    total_students = len(students)

    # Answer basic database questions without an external AI model
    if "how many" in question or "count" in question or "total" in question:
        return {
            "question": prompt,
            "answer": f"There are {total_students} student records in the database."
        }

    if "list" in question or "show" in question or "all students" in question:
        student_list = [
            {
                "id": student.id,
                "name": student.name,
                "course": student.course
            }
            for student in students
        ]

        return {
            "question": prompt,
            "answer": student_list
        }

    if "email" in question:
        matches = db.query(models.Student).filter(
            models.Student.email.isnot(None)
        ).all()

        return {
            "question": prompt,
            "answer": [
                {"name": student.name, "email": student.email}
                for student in matches
            ]
        }

    return {
        "question": prompt,
        "answer": (
            "I can answer basic questions about student counts, "
            "student lists, and email addresses. Try asking one of those."
        )
    }
