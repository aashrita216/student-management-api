from fastapi import APIRouter
from app.routes import create_student, get_students, update_student, delete_student, ai_query

router = APIRouter()

# Registering individual operations to the base layout
router.include_router(create_student.router)
router.include_router(get_students.router)
router.include_router(update_student.router)
router.include_router(delete_student.router)
router.include_router(ai_query.router)