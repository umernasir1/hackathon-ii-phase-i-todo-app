# Task Breakdown: Todo Full-Stack Web Application (Phase II)

**Feature Branch**: `002-phase-ii-web-app`
**Created**: 2025-12-18
**Status**: Ready for Implementation
**Spec Reference**: `specs/phase-ii-web-app/spec.md`
**Plan Reference**: `specs/phase-ii-web-app/plan.md`

---

## Task Execution Order

Tasks are organized in dependency order. Complete tasks sequentially within each phase.

**Phase 1: Setup** → **Phase 2: Database** → **Phase 3: Authentication** → **Phase 4: Backend API** → **Phase 5: Frontend** → **Phase 6: Deployment**

---

# Phase 1: Project Setup

## Task T-001: Create Monorepo Structure

**From**: plan.md §9 (Component Breakdown)
**Spec**: spec.md §Architecture Decisions

**Description**: Set up monorepo folder structure with frontend and backend directories

**Preconditions**:
- Phase I project exists at `D:\PIAIC Batch 76\HackatonII`
- Git repository initialized

**Steps**:
1. Create `frontend/` directory
2. Create `backend/` directory
3. Update root `.gitignore` to include frontend and backend specific ignores
4. Create `frontend/.gitignore` (Next.js specific)
5. Create `backend/.gitignore` (Python specific)
6. Update root `README.md` with monorepo structure documentation

**Expected Outputs**:
- Folder structure:
  ```
  HackatonII/
  ├── frontend/
  ├── backend/
  ├── src/           # Phase I console app (keep for reference)
  ├── specs/
  ├── .specify/
  ├── .gitignore
  └── README.md
  ```

**Artifacts to Modify**:
- `README.md`
- `.gitignore`
- Create: `frontend/.gitignore`
- Create: `backend/.gitignore`

**Acceptance Criteria**:
- [ ] `frontend/` and `backend/` directories exist
- [ ] `.gitignore` files prevent committing node_modules and .venv
- [ ] README documents monorepo structure

**Test Cases**:
- Verify `frontend/` directory exists
- Verify `backend/` directory exists
- Verify `.gitignore` contains `frontend/node_modules` and `backend/.venv`

---

## Task T-002: Initialize Next.js Frontend

**From**: plan.md §9.1 (Frontend Components)
**Spec**: spec.md §Technical Constraints TC-001

**Description**: Create Next.js 16+ application with App Router, TypeScript, and Tailwind CSS

**Preconditions**:
- T-001 completed
- Node.js 18+ installed
- npm/pnpm available

**Steps**:
1. Navigate to `frontend/` directory
2. Run `npx create-next-app@latest . --typescript --tailwind --app --no-src-dir`
3. Accept defaults for: ESLint (yes), Turbopack (no), import alias (yes, @/*)
4. Create `frontend/CLAUDE.md` with frontend-specific instructions
5. Create `frontend/.env.local` template with required variables
6. Update `frontend/package.json` to include project metadata

**Expected Outputs**:
- Next.js 16+ app initialized in `frontend/`
- TypeScript configured
- Tailwind CSS configured
- App Router structure (`app/` directory)

**Artifacts to Modify**:
- Create: `frontend/package.json`
- Create: `frontend/tsconfig.json`
- Create: `frontend/tailwind.config.ts`
- Create: `frontend/next.config.ts`
- Create: `frontend/CLAUDE.md`
- Create: `frontend/.env.local.template`

**Acceptance Criteria**:
- [ ] `npm run dev` starts Next.js dev server on port 3000
- [ ] App uses TypeScript (`.tsx` files)
- [ ] Tailwind CSS classes work
- [ ] App Router structure present (`app/layout.tsx`, `app/page.tsx`)

**Test Cases**:
- Run `cd frontend && npm run dev`
- Open http://localhost:3000
- Verify default Next.js page loads
- Verify no TypeScript errors

---

## Task T-003: Initialize FastAPI Backend

**From**: plan.md §9.2 (Backend Components)
**Spec**: spec.md §Technical Constraints TC-002, TC-003

**Description**: Create FastAPI application with SQLModel, Python 3.13+, and UV package manager

**Preconditions**:
- T-001 completed
- Python 3.13+ installed
- UV package manager installed

**Steps**:
1. Navigate to `backend/` directory
2. Run `uv init .` to initialize Python project
3. Create `backend/pyproject.toml` with dependencies:
   - fastapi
   - uvicorn[standard]
   - sqlmodel
   - psycopg2-binary (PostgreSQL driver)
   - python-jose[cryptography] (JWT)
   - passlib[bcrypt] (password hashing)
   - python-multipart (form data)
   - alembic (migrations)
4. Create `backend/app/` directory structure
5. Create `backend/app/__init__.py`
6. Create `backend/app/main.py` with basic FastAPI app and CORS
7. Create `backend/CLAUDE.md` with backend-specific instructions
8. Create `backend/.env.template` with required variables

**Expected Outputs**:
- FastAPI app initialized in `backend/`
- Dependencies installed via UV
- Basic app structure created

**Artifacts to Modify**:
- Create: `backend/pyproject.toml`
- Create: `backend/app/__init__.py`
- Create: `backend/app/main.py`
- Create: `backend/CLAUDE.md`
- Create: `backend/.env.template`

**Acceptance Criteria**:
- [ ] `uv run uvicorn app.main:app --reload` starts FastAPI on port 8000
- [ ] http://localhost:8000/docs shows Swagger UI
- [ ] CORS configured to allow http://localhost:3000
- [ ] All dependencies installed

**Test Cases**:
- Run `cd backend && uv run uvicorn app.main:app --reload`
- Open http://localhost:8000/docs
- Verify Swagger UI loads
- Test CORS with frontend origin

**Code Reference**:
```python
# backend/app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Todo API", version="2.0.0")

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Todo API - Phase II"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}
```

---

# Phase 2: Database Setup

## Task T-004: Create Neon PostgreSQL Database

**From**: plan.md §5.2 (Database Schema)
**Spec**: spec.md §Technical Constraints TC-004

**Description**: Set up Neon Serverless PostgreSQL database and obtain connection string

**Preconditions**:
- Neon account created (https://neon.tech)
- Email verified

**Steps**:
1. Log in to Neon console
2. Create new project: "hackathon-todo-phase-ii"
3. Select region: Closest to your location
4. Create database: "todo_db"
5. Copy connection string (format: `postgresql://user:pass@host/dbname`)
6. Store connection string in `backend/.env` as `DATABASE_URL`
7. Test connection using `psql` or database client

**Expected Outputs**:
- Neon PostgreSQL database created
- Connection string obtained
- Database accessible

**Artifacts to Modify**:
- Create: `backend/.env` (add `DATABASE_URL`)

**Acceptance Criteria**:
- [ ] Database created in Neon dashboard
- [ ] Connection string works (test with psql or Python)
- [ ] Database is empty (no tables yet)

**Test Cases**:
- Run `psql $DATABASE_URL` (if psql installed)
- Or test with Python:
  ```python
  from sqlmodel import create_engine
  engine = create_engine("postgresql://...")
  with engine.connect() as conn:
      print("Connected successfully")
  ```

**Security Note**:
- Do NOT commit `backend/.env` to git
- Verify `.gitignore` includes `.env`

---

## Task T-005: Create SQLModel Database Models

**From**: plan.md §5.2 (Database Schema)
**Spec**: spec.md §Key Entities

**Description**: Define User and Task SQLModel models with proper relationships

**Preconditions**:
- T-003 completed (FastAPI initialized)
- T-004 completed (Database created)

**Steps**:
1. Create `backend/app/models.py`
2. Define `User` model with fields: id (UUID), email, password_hash, name, created_at, updated_at
3. Define `Task` model with fields: id, user_id (FK), title, description, completed, created_at, updated_at
4. Add validators for title (1-200 chars) and description (0-1000 chars)
5. Add `__repr__` methods for debugging
6. Configure relationships (User has many Tasks)

**Expected Outputs**:
- `models.py` with User and Task classes
- Type hints for all fields
- Validators for constraints

**Artifacts to Modify**:
- Create: `backend/app/models.py`

**Acceptance Criteria**:
- [ ] User model has UUID primary key
- [ ] Task model has foreign key to User
- [ ] Title validation (1-200 chars)
- [ ] Description validation (max 1000 chars)
- [ ] Models inherit from SQLModel with `table=True`

**Test Cases**:
- Import models without errors
- Instantiate User: `User(email="test@example.com", password_hash="...")`
- Instantiate Task: `Task(user_id="...", title="Test")`
- Verify validation raises error for title > 200 chars

**Code Reference**:
```python
# backend/app/models.py
from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime
from typing import Optional
import uuid

class User(SQLModel, table=True):
    __tablename__ = "users"

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    email: str = Field(unique=True, index=True, max_length=255)
    password_hash: str = Field(max_length=255)
    name: Optional[str] = Field(default=None, max_length=100)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    # Relationship
    tasks: list["Task"] = Relationship(back_populates="owner")

class Task(SQLModel, table=True):
    __tablename__ = "tasks"

    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: uuid.UUID = Field(foreign_key="users.id", index=True)
    title: str = Field(min_length=1, max_length=200)
    description: Optional[str] = Field(default="", max_length=1000)
    completed: bool = Field(default=False)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    # Relationship
    owner: Optional[User] = Relationship(back_populates="tasks")
```

---

## Task T-006: Set Up Database Connection and Migrations

**From**: plan.md §5.3 (Schema Evolution)
**Spec**: spec.md §Technical Constraints TC-003

**Description**: Configure SQLModel database connection and set up Alembic for migrations

**Preconditions**:
- T-004 completed (Database created)
- T-005 completed (Models defined)

**Steps**:
1. Create `backend/app/db.py` with database engine and session management
2. Initialize Alembic: `cd backend && uv run alembic init alembic`
3. Update `backend/alembic.ini` with database URL placeholder
4. Update `backend/alembic/env.py` to import SQLModel models
5. Create initial migration: `uv run alembic revision --autogenerate -m "create users and tasks tables"`
6. Review generated migration file
7. Apply migration: `uv run alembic upgrade head`
8. Verify tables created in Neon dashboard

**Expected Outputs**:
- Database connection configured
- Alembic initialized
- Initial migration created and applied
- `users` and `tasks` tables exist in database

**Artifacts to Modify**:
- Create: `backend/app/db.py`
- Create: `backend/alembic.ini`
- Create: `backend/alembic/env.py`
- Create: `backend/alembic/versions/xxxx_create_users_and_tasks_tables.py`

**Acceptance Criteria**:
- [ ] Database engine created successfully
- [ ] Alembic can connect to database
- [ ] Migration creates `users` table with 6 columns
- [ ] Migration creates `tasks` table with 7 columns
- [ ] Foreign key constraint exists on `tasks.user_id`

**Test Cases**:
- Run `uv run alembic upgrade head`
- Verify no errors
- Connect to Neon database
- Run `\dt` to list tables
- Verify `users` and `tasks` exist

**Code Reference**:
```python
# backend/app/db.py
from sqlmodel import create_engine, Session
import os

DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL, echo=True)

def get_session():
    with Session(engine) as session:
        yield session
```

---

# Phase 3: Authentication

## Task T-007: Implement Password Hashing and JWT Utilities

**From**: plan.md §4.3 (Security)
**Spec**: spec.md §NFR-003

**Description**: Create utility functions for password hashing (bcrypt) and JWT token generation/verification

**Preconditions**:
- T-003 completed (FastAPI initialized)
- passlib and python-jose installed

**Steps**:
1. Create `backend/app/auth.py`
2. Implement `hash_password(password: str) -> str` using bcrypt
3. Implement `verify_password(plain: str, hashed: str) -> bool`
4. Implement `create_access_token(data: dict) -> str` for JWT generation
5. Implement `verify_token(token: str) -> dict` for JWT verification
6. Add JWT_SECRET to `backend/.env` (generate random secret)
7. Add TOKEN_EXPIRE_DAYS to config (default: 7 days)

**Expected Outputs**:
- `auth.py` with 4 utility functions
- JWT secret configured
- Password hashing working with bcrypt (cost factor 12)

**Artifacts to Modify**:
- Create: `backend/app/auth.py`
- Update: `backend/.env` (add JWT_SECRET)

**Acceptance Criteria**:
- [ ] `hash_password()` returns bcrypt hash
- [ ] `verify_password()` correctly validates passwords
- [ ] `create_access_token()` generates valid JWT
- [ ] `verify_token()` decodes JWT and returns payload
- [ ] JWT tokens expire after 7 days

**Test Cases**:
- Hash password and verify: `verify_password("test123", hash_password("test123"))` → True
- Create token and decode: `verify_token(create_access_token({"sub": "user_id"}))`→ {"sub": "user_id"}
- Verify invalid token raises exception

**Code Reference**:
```python
# backend/app/auth.py
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
    return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
```

---

## Task T-008: Create Authentication Dependency for FastAPI

**From**: plan.md §3.2 (Error Taxonomy)
**Spec**: spec.md §FR-013

**Description**: Create FastAPI dependency to extract and verify JWT from Authorization header

**Preconditions**:
- T-007 completed (JWT utilities created)
- T-005 completed (User model exists)

**Steps**:
1. Create `backend/app/dependencies.py`
2. Implement `get_current_user(token: str = Depends(oauth2_scheme))` dependency
3. Extract token from Authorization Bearer header
4. Verify JWT token
5. Query database for user by ID from token
6. Raise 401 if token invalid or user not found
7. Return User object

**Expected Outputs**:
- `dependencies.py` with `get_current_user` function
- Dependency ready to use in route handlers

**Artifacts to Modify**:
- Create: `backend/app/dependencies.py`

**Acceptance Criteria**:
- [ ] Extracts token from `Authorization: Bearer <token>` header
- [ ] Returns User object if token valid
- [ ] Raises HTTPException(401) if token invalid
- [ ] Raises HTTPException(401) if user not found

**Test Cases**:
- Call with valid token → returns User
- Call with invalid token → raises 401
- Call with expired token → raises 401
- Call without Authorization header → raises 401

**Code Reference**:
```python
# backend/app/dependencies.py
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlmodel import Session, select
from app.db import get_session
from app.models import User
from app.auth import verify_token
from jose import JWTError

security = HTTPBearer()

async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    session: Session = Depends(get_session)
) -> User:
    token = credentials.credentials
    try:
        payload = verify_token(token)
        user_id: str = payload.get("sub")
        if user_id is None:
            raise HTTPException(status_code=401, detail="Invalid token")
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

    user = session.get(User, user_id)
    if user is None:
        raise HTTPException(status_code=401, detail="User not found")
    return user
```

---

## Task T-009: Implement Register and Login Endpoints

**From**: plan.md §3.1 (API Endpoints - Authentication)
**Spec**: spec.md §User Story 1

**Description**: Create POST /api/auth/register and POST /api/auth/login endpoints

**Preconditions**:
- T-007 completed (Auth utilities)
- T-008 completed (Auth dependency)
- T-006 completed (Database ready)

**Steps**:
1. Create `backend/app/routes/auth.py`
2. Implement `POST /api/auth/register`:
   - Accept email and password
   - Validate email format
   - Check if email already exists
   - Hash password
   - Create user in database
   - Return user data (without password_hash)
3. Implement `POST /api/auth/login`:
   - Accept email and password
   - Query user by email
   - Verify password
   - Generate JWT token
   - Return token and user data
4. Register router in `main.py`

**Expected Outputs**:
- `/api/auth/register` endpoint working
- `/api/auth/login` endpoint working
- JWT tokens returned on successful login

**Artifacts to Modify**:
- Create: `backend/app/routes/auth.py`
- Update: `backend/app/main.py` (include router)

**Acceptance Criteria**:
- [ ] Register creates user in database
- [ ] Register returns 400 if email already exists
- [ ] Login returns JWT token if credentials valid
- [ ] Login returns 401 if credentials invalid
- [ ] Password is hashed before storing

**Test Cases**:
- POST /api/auth/register with {"email": "test@example.com", "password": "test123"} → 201 Created
- POST /api/auth/register with same email → 400 Bad Request
- POST /api/auth/login with correct credentials → 200 OK + token
- POST /api/auth/login with wrong password → 401 Unauthorized

**Code Reference**: (See plan.md §3.1 for detailed API contracts)

---

## Task T-010: Set Up Better Auth in Frontend

**From**: plan.md §2 (Decision 2: Authentication Strategy)
**Spec**: spec.md §Technical Constraints TC-005

**Description**: Configure Better Auth in Next.js frontend with JWT token management

**Preconditions**:
- T-002 completed (Next.js initialized)
- T-009 completed (Backend auth endpoints ready)

**Steps**:
1. Install Better Auth: `cd frontend && npm install better-auth`
2. Create `frontend/lib/auth.ts` with Better Auth config
3. Configure JWT plugin
4. Set BETTER_AUTH_SECRET in `frontend/.env.local` (same as backend JWT_SECRET)
5. Create `frontend/app/api/auth/[...all]/route.ts` for Better Auth routes
6. Create auth context/provider in `frontend/lib/auth-provider.tsx`
7. Wrap app in auth provider in `frontend/app/layout.tsx`
8. Create `frontend/lib/api.ts` for authenticated API calls

**Expected Outputs**:
- Better Auth configured
- Auth provider wrapping app
- API client with automatic token injection

**Artifacts to Modify**:
- Create: `frontend/lib/auth.ts`
- Create: `frontend/app/api/auth/[...all]/route.ts`
- Create: `frontend/lib/auth-provider.tsx`
- Update: `frontend/app/layout.tsx`
- Create: `frontend/lib/api.ts`
- Update: `frontend/.env.local`

**Acceptance Criteria**:
- [ ] Better Auth initialized
- [ ] JWT tokens stored in httpOnly cookies
- [ ] Auth state accessible via useAuth() hook
- [ ] API client includes Authorization header automatically

**Test Cases**:
- Call login() from frontend → receives JWT token
- Check localStorage/cookies for token
- Make authenticated API call → Authorization header present

---

# Phase 4: Backend API Implementation

## Task T-011: Implement GET /api/{user_id}/tasks Endpoint

**From**: plan.md §3.1 (Endpoint 1)
**Spec**: spec.md §User Story 3

**Description**: Create endpoint to list all tasks for authenticated user

**Preconditions**:
- T-008 completed (Auth dependency)
- T-006 completed (Database ready)

**Steps**:
1. Create `backend/app/routes/tasks.py`
2. Implement `GET /api/{user_id}/tasks`:
   - Verify user_id in path matches current user from JWT
   - Query all tasks where user_id = current_user.id
   - Return tasks array with total/completed/pending counts
   - Order by created_at DESC
3. Add error handling for user_id mismatch (403 Forbidden)
4. Register router in `main.py`

**Expected Outputs**:
- Endpoint returns JSON array of tasks
- Only authenticated user's tasks returned
- Proper error handling

**Artifacts to Modify**:
- Create: `backend/app/routes/tasks.py`
- Update: `backend/app/main.py`

**Acceptance Criteria**:
- [ ] Returns all tasks for authenticated user
- [ ] Returns empty array if user has no tasks
- [ ] Returns 403 if path user_id doesn't match JWT user_id
- [ ] Returns 401 if no valid JWT token

**Test Cases**:
- GET /api/user_123/tasks with valid token → 200 + tasks array
- GET /api/user_456/tasks with user_123 token → 403 Forbidden
- GET /api/user_123/tasks without token → 401 Unauthorized

**Code Reference**: (See plan.md §3.1 Endpoint 1 for response format)

---

## Task T-012: Implement POST /api/{user_id}/tasks Endpoint

**From**: plan.md §3.1 (Endpoint 2)
**Spec**: spec.md §User Story 2

**Description**: Create endpoint to add new task

**Preconditions**:
- T-011 completed (Tasks router exists)

**Steps**:
1. Add `POST /api/{user_id}/tasks` to `tasks.py`
2. Accept request body with title and description
3. Verify user_id matches current user
4. Validate title (1-200 chars) and description (max 1000 chars)
5. Create task in database with user_id from JWT
6. Return created task with 201 status
7. Handle validation errors (400 Bad Request)

**Expected Outputs**:
- Endpoint creates task in database
- Returns created task with assigned ID
- Proper validation errors

**Artifacts to Modify**:
- Update: `backend/app/routes/tasks.py`

**Acceptance Criteria**:
- [ ] Creates task with title only (description optional)
- [ ] Returns 201 Created with task object
- [ ] Returns 400 if title missing or > 200 chars
- [ ] Returns 400 if description > 1000 chars
- [ ] Task automatically assigned to current user

**Test Cases**:
- POST with {"title": "Test"} → 201 Created
- POST with {"title": "Test", "description": "Details"} → 201 Created
- POST with {"description": "No title"} → 400 Bad Request
- POST with {"title": "a" * 201} → 400 Bad Request

---

## Task T-013: Implement PUT /api/{user_id}/tasks/{id} Endpoint

**From**: plan.md §3.1 (Endpoint 4)
**Spec**: spec.md §User Story 5

**Description**: Create endpoint to update task title and description

**Preconditions**:
- T-012 completed (POST endpoint exists)

**Steps**:
1. Add `PUT /api/{user_id}/tasks/{id}` to `tasks.py`
2. Verify user_id matches current user
3. Query task by ID
4. Verify task belongs to current user (403 if not)
5. Update title and/or description
6. Update `updated_at` timestamp
7. Save to database
8. Return updated task

**Expected Outputs**:
- Endpoint updates task in database
- Returns updated task
- Proper authorization checks

**Artifacts to Modify**:
- Update: `backend/app/routes/tasks.py`

**Acceptance Criteria**:
- [ ] Updates task title
- [ ] Updates task description
- [ ] Returns 404 if task doesn't exist
- [ ] Returns 403 if task belongs to different user
- [ ] Updates `updated_at` timestamp

**Test Cases**:
- PUT /api/user_123/tasks/1 with {"title": "New title"} → 200 OK
- PUT /api/user_123/tasks/999 → 404 Not Found
- PUT /api/user_123/tasks/1 (task owned by user_456) → 403 Forbidden

---

## Task T-014: Implement DELETE /api/{user_id}/tasks/{id} Endpoint

**From**: plan.md §3.1 (Endpoint 5)
**Spec**: spec.md §User Story 6

**Description**: Create endpoint to delete task

**Preconditions**:
- T-013 completed (PUT endpoint exists)

**Steps**:
1. Add `DELETE /api/{user_id}/tasks/{id}` to `tasks.py`
2. Verify user_id matches current user
3. Query task by ID
4. Verify task belongs to current user
5. Delete task from database
6. Return 204 No Content

**Expected Outputs**:
- Endpoint deletes task from database
- Returns 204 status (no content)

**Artifacts to Modify**:
- Update: `backend/app/routes/tasks.py`

**Acceptance Criteria**:
- [ ] Deletes task from database
- [ ] Returns 204 No Content
- [ ] Returns 404 if task doesn't exist
- [ ] Returns 403 if task belongs to different user
- [ ] Idempotent (deleting twice returns same result)

**Test Cases**:
- DELETE /api/user_123/tasks/1 → 204 No Content
- DELETE /api/user_123/tasks/1 again → 404 Not Found
- DELETE /api/user_123/tasks/1 (owned by user_456) → 403 Forbidden

---

## Task T-015: Implement PATCH /api/{user_id}/tasks/{id}/complete Endpoint

**From**: plan.md §3.1 (Endpoint 6)
**Spec**: spec.md §User Story 4

**Description**: Create endpoint to toggle task completion status

**Preconditions**:
- T-014 completed (DELETE endpoint exists)

**Steps**:
1. Add `PATCH /api/{user_id}/tasks/{id}/complete` to `tasks.py`
2. Accept request body with `completed` boolean
3. Verify user_id and task ownership
4. Update task completed status
5. Update `updated_at` timestamp
6. Return updated task

**Expected Outputs**:
- Endpoint updates completion status
- Returns updated task with new status

**Artifacts to Modify**:
- Update: `backend/app/routes/tasks.py`

**Acceptance Criteria**:
- [ ] Updates completed status
- [ ] Returns 200 with updated task
- [ ] Returns 400 if completed not boolean
- [ ] Returns 403 if not task owner

**Test Cases**:
- PATCH with {"completed": true} → 200 OK, task.completed = true
- PATCH with {"completed": false} → 200 OK, task.completed = false
- PATCH with {"completed": "yes"} → 400 Bad Request

---

## Task T-016: Test All API Endpoints with Postman

**From**: plan.md §10 (Testing Strategy)
**Spec**: spec.md §Success Criteria SC-004

**Description**: Comprehensive API testing using Postman collection

**Preconditions**:
- T-009 through T-015 completed (All endpoints implemented)

**Steps**:
1. Create Postman collection "Todo API Phase II"
2. Create environment variables: baseUrl, userId, token
3. Test auth endpoints:
   - Register new user
   - Login and capture token
4. Test task endpoints (with token):
   - Create task
   - List tasks
   - Update task
   - Mark complete
   - Delete task
5. Test authorization (user A can't access user B's tasks)
6. Test validation (invalid inputs return 400)
7. Export collection to `backend/postman_collection.json`

**Expected Outputs**:
- All API endpoints working correctly
- Authorization enforced
- Validation working
- Postman collection exported

**Artifacts to Modify**:
- Create: `backend/postman_collection.json`

**Acceptance Criteria**:
- [ ] All 8 endpoints (2 auth + 6 tasks) return expected responses
- [ ] User cannot access other user's tasks
- [ ] Invalid inputs return proper error messages
- [ ] All tests pass

**Test Cases**: (See plan.md §3.1 for detailed test cases per endpoint)

---

# Phase 5: Frontend Implementation

## Task T-017: Create Login and Register Pages

**From**: plan.md §9.1 (Frontend Components)
**Spec**: spec.md §User Story 1

**Description**: Build authentication UI with login and register forms

**Preconditions**:
- T-010 completed (Better Auth configured)
- T-009 completed (Backend auth endpoints ready)

**Steps**:
1. Create `frontend/app/login/page.tsx`
2. Create `frontend/components/LoginForm.tsx` with:
   - Email input
   - Password input
   - Submit button
   - Error display
   - Link to register page
3. Create `frontend/app/register/page.tsx`
4. Create `frontend/components/RegisterForm.tsx`
5. Implement form validation (email format, password min length)
6. Call Better Auth login/register functions
7. Redirect to /dashboard on success
8. Display errors on failure

**Expected Outputs**:
- Login page at `/login`
- Register page at `/register`
- Forms with validation
- Better Auth integration working

**Artifacts to Modify**:
- Create: `frontend/app/login/page.tsx`
- Create: `frontend/app/register/page.tsx`
- Create: `frontend/components/LoginForm.tsx`
- Create: `frontend/components/RegisterForm.tsx`

**Acceptance Criteria**:
- [ ] User can register with email/password
- [ ] User can login with credentials
- [ ] Validation shows errors for invalid inputs
- [ ] Successful login redirects to /dashboard
- [ ] Failed login shows error message

**Test Cases**:
- Register new user → redirects to dashboard
- Register with existing email → shows error
- Login with correct credentials → redirects to dashboard
- Login with wrong password → shows error

---

## Task T-018: Create Dashboard Layout and Navbar

**From**: plan.md §9.1 (Frontend Components)
**Spec**: spec.md §FR-014

**Description**: Build main dashboard layout with navigation bar

**Preconditions**:
- T-017 completed (Auth pages created)
- T-010 completed (Auth provider setup)

**Steps**:
1. Create `frontend/app/dashboard/layout.tsx`
2. Create `frontend/components/Navbar.tsx` with:
   - App title/logo
   - User email display
   - Logout button
3. Implement logout functionality
4. Add protected route logic (redirect to /login if not authenticated)
5. Style with Tailwind CSS (responsive design)

**Expected Outputs**:
- Dashboard layout with navbar
- Logout working
- Protected routes

**Artifacts to Modify**:
- Create: `frontend/app/dashboard/layout.tsx`
- Create: `frontend/components/Navbar.tsx`

**Acceptance Criteria**:
- [ ] Navbar displays user email
- [ ] Logout button clears session and redirects to login
- [ ] Dashboard only accessible when authenticated
- [ ] Responsive on mobile and desktop

**Test Cases**:
- Access /dashboard while logged in → shows dashboard
- Access /dashboard while logged out → redirects to /login
- Click logout → redirects to /login

---

## Task T-019: Implement Task List Component

**From**: plan.md §9.1 (Frontend Components)
**Spec**: spec.md §User Story 3

**Description**: Create component to display list of tasks

**Preconditions**:
- T-018 completed (Dashboard layout created)
- T-011 completed (GET tasks endpoint ready)

**Steps**:
1. Create `frontend/app/dashboard/page.tsx`
2. Create `frontend/components/TaskList.tsx`
3. Fetch tasks from API on component mount
4. Display tasks in a list/grid layout
5. Show empty state if no tasks
6. Create `frontend/components/TaskItem.tsx` for individual task
7. Display task title, description, completion status
8. Add loading state
9. Add error handling

**Expected Outputs**:
- Dashboard page displaying tasks
- TaskList component fetching and rendering tasks
- Empty state for no tasks
- Loading and error states

**Artifacts to Modify**:
- Create: `frontend/app/dashboard/page.tsx`
- Create: `frontend/components/TaskList.tsx`
- Create: `frontend/components/TaskItem.tsx`

**Acceptance Criteria**:
- [ ] Fetches tasks from GET /api/{user_id}/tasks
- [ ] Displays all tasks
- [ ] Shows "No tasks yet" if empty
- [ ] Shows loading spinner while fetching
- [ ] Shows error message if API call fails
- [ ] Completed tasks visually distinguished (strikethrough)

**Test Cases**:
- Load dashboard with tasks → displays all tasks
- Load dashboard with no tasks → shows empty state
- Backend down → shows error message

---

## Task T-020: Implement Add Task Form

**From**: plan.md §9.1 (Frontend Components)
**Spec**: spec.md §User Story 2

**Description**: Create form to add new tasks

**Preconditions**:
- T-019 completed (Task list created)
- T-012 completed (POST task endpoint ready)

**Steps**:
1. Create `frontend/components/AddTaskForm.tsx`
2. Add form with:
   - Title input (required, max 200 chars)
   - Description textarea (optional, max 1000 chars)
   - Submit button
   - Cancel button
3. Implement form validation
4. Call POST /api/{user_id}/tasks on submit
5. Refresh task list on success
6. Show success/error messages
7. Clear form on success
8. Add to dashboard page (modal or inline)

**Expected Outputs**:
- Add task form component
- Form validation working
- New tasks created via API
- Task list refreshes

**Artifacts to Modify**:
- Create: `frontend/components/AddTaskForm.tsx`
- Update: `frontend/app/dashboard/page.tsx` (include form)

**Acceptance Criteria**:
- [ ] User can enter title and description
- [ ] Submitting creates task via API
- [ ] Task list updates with new task
- [ ] Form shows validation errors
- [ ] Form clears after successful submission

**Test Cases**:
- Submit with valid title → task created
- Submit with empty title → shows error
- Submit with title > 200 chars → shows error
- Submit with description > 1000 chars → shows error

---

## Task T-021: Implement Task Edit and Delete Actions

**From**: plan.md §9.1 (Frontend Components)
**Spec**: spec.md §User Stories 5, 6

**Description**: Add edit and delete functionality to tasks

**Preconditions**:
- T-019 completed (Task list created)
- T-013, T-014 completed (PUT, DELETE endpoints ready)

**Steps**:
1. Add Edit button to TaskItem component
2. Create `frontend/components/EditTaskModal.tsx`
3. Pre-fill form with existing task data
4. Call PUT /api/{user_id}/tasks/{id} on submit
5. Add Delete button to TaskItem
6. Create `frontend/components/DeleteConfirmModal.tsx`
7. Call DELETE /api/{user_id}/tasks/{id} on confirm
8. Refresh task list after edit/delete
9. Handle errors

**Expected Outputs**:
- Edit modal working
- Delete confirmation working
- Task list updates after changes

**Artifacts to Modify**:
- Create: `frontend/components/EditTaskModal.tsx`
- Create: `frontend/components/DeleteConfirmModal.tsx`
- Update: `frontend/components/TaskItem.tsx` (add buttons)

**Acceptance Criteria**:
- [ ] Edit button opens modal with task data
- [ ] Saving edits updates task via API
- [ ] Delete button shows confirmation dialog
- [ ] Confirming delete removes task
- [ ] Task list refreshes after both operations

**Test Cases**:
- Click edit → modal opens with task data
- Edit title and save → task updated
- Click delete and confirm → task removed
- Click delete and cancel → task remains

---

## Task T-022: Implement Task Completion Toggle

**From**: plan.md §9.1 (Frontend Components)
**Spec**: spec.md §User Story 4

**Description**: Add checkbox to toggle task completion

**Preconditions**:
- T-019 completed (Task list created)
- T-015 completed (PATCH complete endpoint ready)

**Steps**:
1. Add checkbox to TaskItem component
2. Bind checkbox to task.completed state
3. Call PATCH /api/{user_id}/tasks/{id}/complete on change
4. Update UI immediately (optimistic update)
5. Revert on API error
6. Apply strikethrough style to completed tasks

**Expected Outputs**:
- Checkbox toggles completion
- API called on change
- UI updates immediately

**Artifacts to Modify**:
- Update: `frontend/components/TaskItem.tsx`

**Acceptance Criteria**:
- [ ] Checkbox reflects task completion status
- [ ] Clicking checkbox calls API
- [ ] Completed tasks show strikethrough
- [ ] UI updates optimistically (no loading delay)
- [ ] Reverts on API error

**Test Cases**:
- Click checkbox on pending task → marked complete
- Click checkbox on complete task → marked pending
- Toggle with backend down → shows error, reverts change

---

# Phase 6: Deployment

## Task T-023: Add Responsive Styling with Tailwind CSS

**From**: plan.md §4.1 (Performance)
**Spec**: spec.md §SC-006

**Description**: Ensure all components are responsive (320px to 2560px)

**Preconditions**:
- T-017 through T-022 completed (All UI components created)

**Steps**:
1. Review all components for responsive design
2. Use Tailwind breakpoints (sm, md, lg, xl)
3. Test on mobile (320px), tablet (768px), desktop (1920px)
4. Ensure forms are usable on mobile
5. Ensure task list readable on all screens
6. Add mobile menu for navbar if needed
7. Test with Chrome DevTools device emulation

**Expected Outputs**:
- All pages responsive
- Mobile-friendly forms
- Readable on all screen sizes

**Artifacts to Modify**:
- Update: All component files (add responsive classes)

**Acceptance Criteria**:
- [ ] App usable on 320px width (iPhone SE)
- [ ] App usable on 768px width (iPad)
- [ ] App usable on 1920px width (desktop)
- [ ] No horizontal scrolling on mobile
- [ ] Touch targets at least 44px (mobile accessibility)

**Test Cases**:
- Open app on mobile → all content visible
- Open app on tablet → optimal layout
- Open app on desktop → full features visible

---

## Task T-024: Deploy Frontend to Vercel

**From**: plan.md §6.4 (Deployment Strategy)
**Spec**: spec.md §FR-015

**Description**: Deploy Next.js frontend to Vercel

**Preconditions**:
- T-023 completed (UI ready)
- Vercel account created
- GitHub repository pushed

**Steps**:
1. Connect GitHub repo to Vercel
2. Configure build settings:
   - Framework: Next.js
   - Root directory: `frontend/`
3. Set environment variables in Vercel:
   - `NEXT_PUBLIC_API_URL`: Backend production URL
   - `BETTER_AUTH_SECRET`: Shared secret
4. Deploy via Vercel dashboard or `vercel deploy --prod`
5. Verify deployment successful
6. Test production app
7. Configure custom domain (optional)

**Expected Outputs**:
- Frontend deployed to Vercel
- Public URL available (e.g., https://todo-phase-ii.vercel.app)
- Environment variables configured

**Artifacts to Modify**:
- Create: `frontend/vercel.json` (optional config)
- Update: README.md (add deployment URL)

**Acceptance Criteria**:
- [ ] App accessible via Vercel URL
- [ ] Environment variables working
- [ ] Build succeeds without errors
- [ ] All pages load correctly

**Test Cases**:
- Visit Vercel URL → app loads
- Register new user → works
- Login → works
- Create task → works (calls backend API)

---

## Task T-025: Deploy Backend to Railway/Render

**From**: plan.md §6.4 (Deployment Strategy)
**Spec**: spec.md §FR-016

**Description**: Deploy FastAPI backend to Railway or Render

**Preconditions**:
- T-016 completed (API tested)
- Railway/Render account created
- Neon database ready

**Steps**:
1. Create new project on Railway/Render
2. Connect GitHub repository
3. Configure build settings:
   - Build command: `pip install -r requirements.txt`
   - Start command: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
   - Root directory: `backend/`
4. Set environment variables:
   - `DATABASE_URL`: Neon connection string
   - `JWT_SECRET`: Same as Better Auth secret
   - `CORS_ORIGINS`: Vercel frontend URL
5. Deploy
6. Run migrations: `alembic upgrade head`
7. Test API health endpoint
8. Update frontend env var with backend URL

**Expected Outputs**:
- Backend deployed and running
- Public API URL (e.g., https://todo-api.railway.app)
- Database migrations applied

**Artifacts to Modify**:
- Create: `backend/requirements.txt` (if not exists)
- Create: `backend/Procfile` or `railway.toml` (platform config)
- Update: README.md (add API URL)

**Acceptance Criteria**:
- [ ] API accessible via public URL
- [ ] /health endpoint returns 200
- [ ] /docs (Swagger) accessible
- [ ] CORS allows frontend origin
- [ ] Database connected

**Test Cases**:
- Visit API URL/health → {"status": "healthy"}
- Visit API URL/docs → Swagger UI loads
- Frontend calls API → CORS allows request
- Create task from frontend → works end-to-end

---

## Final Verification Checklist

After completing all tasks, verify:

**Functionality**:
- [ ] User can register and login
- [ ] User can view their tasks
- [ ] User can add tasks
- [ ] User can edit tasks
- [ ] User can delete tasks
- [ ] User can mark tasks complete/incomplete
- [ ] User A cannot see User B's tasks

**Technical**:
- [ ] All API endpoints return correct status codes
- [ ] JWT authentication working
- [ ] Database persistence working
- [ ] Frontend responsive (mobile + desktop)
- [ ] No console errors in browser
- [ ] No server errors in logs

**Deployment**:
- [ ] Frontend deployed to Vercel
- [ ] Backend deployed to Railway/Render
- [ ] Both accessible via public URLs
- [ ] End-to-end flow working in production

**Documentation**:
- [ ] README updated with setup instructions
- [ ] Environment variables documented
- [ ] API endpoints documented
- [ ] Deployment URLs included

---

## Implementation Notes

**Dependencies Between Tasks**:
- Tasks within a phase can sometimes be parallelized
- Must complete Phase 1 before Phase 2
- Authentication (Phase 3) must complete before API (Phase 4)
- Backend API must complete before Frontend (Phase 5)

**Estimated Timeline**:
- Phase 1 (Setup): 1-2 hours
- Phase 2 (Database): 2-3 hours
- Phase 3 (Auth): 3-4 hours
- Phase 4 (Backend API): 4-5 hours
- Phase 5 (Frontend): 5-6 hours
- Phase 6 (Deployment): 1-2 hours
- **Total**: 16-22 hours of focused work

**Spec-Driven Workflow**:
For each task:
1. Read task description and references
2. Review acceptance criteria
3. Use Claude Code to generate implementation
4. Test against test cases
5. Mark task complete only when all criteria pass

---

**Next Action**: Begin implementation with Task T-001
