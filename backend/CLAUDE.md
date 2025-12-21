# Backend Development Rules

This is the FastAPI backend for the Todo Full-Stack Web Application (Phase II).

## Technology Stack

- **Framework**: FastAPI
- **Language**: Python 3.13+
- **ORM**: SQLModel
- **Database**: Neon PostgreSQL (Serverless)
- **Authentication**: JWT tokens (python-jose)
- **Password Hashing**: Bcrypt (passlib)
- **Migrations**: Alembic
- **Package Manager**: UV

## Project Structure

```
backend/
├── app/
│   ├── __init__.py
│   ├── main.py            # FastAPI application entry point
│   ├── db.py              # Database connection and engine
│   ├── models.py          # SQLModel database models
│   ├── auth.py            # Authentication utilities
│   ├── dependencies.py    # Dependency injection functions
│   └── routes/            # API route handlers
│       ├── __init__.py
│       ├── auth.py        # /auth/register, /auth/login
│       └── tasks.py       # /api/{user_id}/tasks CRUD
├── alembic/               # Database migrations
│   ├── versions/
│   └── env.py
├── tests/                 # API tests
├── .env.example           # Environment template
├── pyproject.toml         # UV dependencies
├── alembic.ini            # Alembic configuration
├── CLAUDE.md              # This file
└── README.md              # Setup instructions

## Development Guidelines

### 1. API Design
- Use RESTful conventions (GET, POST, PUT, DELETE)
- Return consistent JSON responses
- Use proper HTTP status codes (200, 201, 400, 401, 404, 500)
- Include detailed error messages in development

### 2. Authentication & Authorization
- Verify JWT token on every protected endpoint
- Extract user_id from token payload
- Validate that path user_id matches token user_id
- Return 401 for invalid/expired tokens, 403 for mismatched user_id

### 3. Database Operations
- Use SQLModel for all database queries
- Use session dependency injection
- Handle database errors gracefully
- Use transactions for multi-step operations

### 4. Data Validation
- Use Pydantic models for request/response validation
- Validate title length (1-200 chars)
- Validate description length (0-1000 chars)
- Return 400 Bad Request for validation errors

### 5. Security
- Never return password hashes in responses
- Use parameterized queries (SQLModel does this)
- Validate and sanitize all inputs
- Set secure CORS policies
- Store secrets in environment variables

### 6. Error Handling
- Use try-except blocks for database operations
- Log errors with proper context
- Return user-friendly error messages
- Don't expose internal implementation details

### 7. Testing
- Write tests for all API endpoints
- Test authentication flows
- Test authorization (user isolation)
- Test edge cases and error conditions

## Code Standards

### Model Example
```python
# app/models.py
from sqlmodel import Field, SQLModel, Relationship
from datetime import datetime
from typing import Optional
import uuid

class User(SQLModel, table=True):
    __tablename__ = "users"

    id: str = Field(default_factory=lambda: str(uuid.uuid4()), primary_key=True)
    email: str = Field(unique=True, index=True)
    password_hash: str
    name: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    tasks: list["Task"] = Relationship(back_populates="user")

class Task(SQLModel, table=True):
    __tablename__ = "tasks"

    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: str = Field(foreign_key="users.id", index=True)
    title: str = Field(max_length=200)
    description: Optional[str] = Field(default=None, max_length=1000)
    completed: bool = Field(default=False, index=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    user: User = Relationship(back_populates="tasks")
```

### Route Example
```python
# app/routes/tasks.py
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from app.models import Task
from app.dependencies import get_current_user, get_session

router = APIRouter()

@router.get("/api/{user_id}/tasks")
async def get_tasks(
    user_id: str,
    current_user: dict = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    # Verify user_id matches token
    if current_user["user_id"] != user_id:
        raise HTTPException(status_code=403, detail="Forbidden")

    # Query tasks
    statement = select(Task).where(Task.user_id == user_id)
    tasks = session.exec(statement).all()

    return {
        "tasks": tasks,
        "total": len(tasks),
        "completed": sum(1 for t in tasks if t.completed),
        "pending": sum(1 for t in tasks if not t.completed)
    }
```

### Authentication Example
```python
# app/auth.py
from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta
import os

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
SECRET_KEY = os.getenv("JWT_SECRET")
ALGORITHM = "HS256"
TOKEN_EXPIRE_DAYS = 7

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(days=TOKEN_EXPIRE_DAYS)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def verify_token(token: str) -> dict:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
```

### Dependency Example
```python
# app/dependencies.py
from fastapi import Depends, HTTPException, Header
from sqlmodel import Session
from app.db import get_session
from app.auth import verify_token

async def get_current_user(authorization: str = Header(...)):
    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Invalid authorization header")

    token = authorization.replace("Bearer ", "")
    payload = verify_token(token)
    return payload
```

## Environment Variables

Create `.env` with:
```
DATABASE_URL=postgresql://user:password@host/database?sslmode=require
JWT_SECRET=your-super-secret-jwt-key-change-this
CORS_ORIGINS=http://localhost:3000,https://your-frontend.vercel.app
```

## Database Commands

```bash
# Create migration
uv run alembic revision --autogenerate -m "description"

# Apply migrations
uv run alembic upgrade head

# Rollback migration
uv run alembic downgrade -1

# Run development server
uv run uvicorn app.main:app --reload --port 8000
```

## Testing Checklist

- [ ] All endpoints require valid JWT (except /auth/register and /auth/login)
- [ ] User isolation enforced (users can only access their own data)
- [ ] Passwords are hashed before storage
- [ ] Validation errors return 400 with clear messages
- [ ] Database errors are handled gracefully
- [ ] CORS allows frontend origin
- [ ] API documentation available at /docs
- [ ] Health check endpoint returns 200

## API Endpoints Summary

### Public Endpoints
- `POST /auth/register` - Create new user account
- `POST /auth/login` - Authenticate and receive JWT token

### Protected Endpoints (require JWT)
- `GET /api/{user_id}/tasks` - Get all user's tasks
- `POST /api/{user_id}/tasks` - Create new task
- `GET /api/{user_id}/tasks/{task_id}` - Get specific task
- `PUT /api/{user_id}/tasks/{task_id}` - Update task
- `DELETE /api/{user_id}/tasks/{task_id}` - Delete task

### Utility Endpoints
- `GET /` - API info
- `GET /health` - Health check

## References

- FastAPI Documentation: https://fastapi.tiangolo.com
- SQLModel Documentation: https://sqlmodel.tiangolo.com
- Alembic Documentation: https://alembic.sqlalchemy.org
- Neon PostgreSQL: https://neon.tech/docs
- Project Spec: `../specs/phase-ii-web-app/spec.md`
- Implementation Plan: `../specs/phase-ii-web-app/plan.md`
- Task List: `../specs/phase-ii-web-app/tasks.md`
