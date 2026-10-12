from fastapi import FastAPI
from app.routes.base import router as api_router
from app.database import engine
from app import models

# Automatically build database tables on server start
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Student Management API")

# Connect our main application instance to our new modular routes layout
app.include_router(api_router)

@app.get("/")
def root():
    return {"message": "Welcome to the Student Management API! Go to /docs for Swagger UI."}