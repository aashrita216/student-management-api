# Student Management API

A Python backend project built using FastAPI and SQLite to manage student records through REST API endpoints. The project also includes an AI Query endpoint for asking questions about student data.

## Features

- Create new student records
- Retrieve all student records
- Retrieve a student by ID
- Update student details
- Delete student records
- Interactive API documentation using Swagger UI
- SQLite database integration
- Modular project structure
- Additional AI Query endpoint

## Technologies Used

- Python
- FastAPI
- SQLite
- SQLAlchemy
- Pydantic
- Uvicorn

## Project Structure

```text
student_management_api/
├── app/
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── ai_query.py
│   │   ├── base.py
│   │   ├── create_student.py
│   │   ├── delete_student.py
│   │   ├── get_students.py
│   │   └── update_student.py
│   ├── database.py
│   ├── models.py
│   └── schemas.py
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/aashrita216/student-management-api.git
cd student-management-api
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

For Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

For Windows Command Prompt:

```cmd
venv\Scripts\activate.bat
```

### 4. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

## Running the Application

Start the FastAPI development server:

```bash
python -m uvicorn main:app --reload
```

After starting the server, open the following links:

- **Swagger UI:** http://127.0.0.1:8000/docs
- **OpenAPI Documentation:** http://127.0.0.1:8000/openapi.json
- **Root Endpoint:** http://127.0.0.1:8000/

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/students` | Retrieve all students |
| POST | `/students` | Create a new student |
| GET | `/students/{student_id}` | Retrieve a student by ID |
| PUT | `/students/{student_id}` | Update student details |
| DELETE | `/students/{student_id}` | Delete a student |
| POST | `/ai/query` | Ask a question using the AI Query endpoint |

## Testing the API

1. Start the application.
2. Open Swagger UI at http://127.0.0.1:8000/docs.
3. Select an endpoint and click **Try it out**.
4. Enter the required request body or student ID.
5. Click **Execute** to send the request.
6. Check the response and verify that the operation worked correctly.

Test creating, retrieving, updating, and deleting student records using sample data.

## Database

The project uses SQLite for storing student records and SQLAlchemy for database operations. Database tables are initialized when the application starts.

## Author

**Aashrita Pothabattula**

GitHub: [aashrita216](https://github.com/aashrita216)

Project Repository: [Student Management API](https://github.com/aashrita216/student-management-api)