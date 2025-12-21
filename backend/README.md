# Todo App - Backend

FastAPI backend for the Todo Full-Stack Web Application (Phase II).

## Tech Stack

- **Framework**: FastAPI
- **Language**: Python 3.13+
- **ORM**: SQLModel
- **Database**: Neon PostgreSQL (Serverless)
- **Authentication**: JWT tokens (python-jose)
- **Password Hashing**: Bcrypt (passlib)
- **Migrations**: Alembic
- **Package Manager**: UV

## Prerequisites

- Python 3.13+
- UV package manager
- Neon PostgreSQL database (or local PostgreSQL)

## Setup

### Step 1: Create Neon PostgreSQL Database

1. **Sign up for Neon** (if you haven't already)
   - Go to [https://console.neon.tech](https://console.neon.tech)
   - Sign up with GitHub, Google, or email

2. **Create a new project**
   - Click "New Project"
   - Name: "hackathon-todo-app"
   - Region: Choose closest to you
   - PostgreSQL version: 16 (latest)
   - Click "Create Project"

3. **Get connection string**
   - After project creation, copy the connection string
   - It looks like: `postgresql://username:password@ep-xxx-xxx.region.aws.neon.tech/neondb?sslmode=require`
   - Save this for Step 3

### Step 2: Install Dependencies

**Option A: Using pip (Recommended for Windows)**
```bash
cd backend
pip install -r requirements.txt
```

**Option B: Using UV package manager**
```bash
# Install UV first (if not installed)
# Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install dependencies
uv sync
```

### Step 3: Configure Environment Variables

1. **Edit the `.env` file** (already created at `backend/.env`):
   ```bash
   # Replace with your Neon connection string from Step 1
   DATABASE_URL=postgresql://user:password@ep-xxx-xxx.region.aws.neon.tech/neondb?sslmode=require

   # Generate a secure JWT secret: openssl rand -hex 32
   JWT_SECRET=your-super-secret-jwt-key-change-this-in-production
   JWT_ALGORITHM=HS256
   ACCESS_TOKEN_EXPIRE_DAYS=7

   # Frontend URL for CORS
   FRONTEND_URL=http://localhost:3000
   ```

2. **Generate a secure JWT secret** (recommended):
   ```bash
   # On Windows (Git Bash or WSL):
   openssl rand -hex 32

   # Or use Python:
   python -c "import secrets; print(secrets.token_hex(32))"
   ```

### Step 4: Run Database Migrations

```bash
cd backend
python -m alembic upgrade head
```

This will create the `users` and `tasks` tables in your Neon database.

### Step 5: Start Development Server

```bash
cd backend
python -m uvicorn main:app --reload --port 8000
```

API documentation will be available at: [http://localhost:8000/docs](http://localhost:8000/docs)

### Verification

Test the API is running:
```bash
curl http://localhost:8000/health
# Should return: {"status":"healthy"}
```

## Development

### Project Structure
```
backend/
├── app/
│   ├── __init__.py
│   ├── config.py        # Settings from environment
│   ├── database.py      # Database connection and session
│   ├── models.py        # SQLModel User and Task models
│   ├── auth.py          # JWT and password hashing utilities
│   └── routers/         # API route handlers
│       ├── __init__.py
│       ├── auth.py      # POST /auth/register, /auth/login
│       └── tasks.py     # CRUD endpoints for /api/{user_id}/tasks
├── alembic/             # Database migrations
│   ├── versions/        # Migration scripts
│   ├── env.py           # Alembic environment config
│   └── script.py.mako   # Migration template
├── main.py              # FastAPI application entry point
├── requirements.txt     # Python dependencies
├── alembic.ini          # Alembic configuration
├── .env                 # Environment variables (not committed)
├── .env.example         # Environment template
└── README.md            # This file
```

### Key Files
- `main.py` - FastAPI app with CORS, lifespan events, and routers
- `app/models.py` - User and Task SQLModel database models + Pydantic schemas
- `app/auth.py` - Password hashing (bcrypt) and JWT token utilities
- `app/database.py` - Database engine, session management, and table creation
- `app/config.py` - Pydantic Settings for environment variables
- `app/routers/auth.py` - Registration and login endpoints
- `app/routers/tasks.py` - Full CRUD operations for tasks

### Database Migrations
```bash
# Create new migration
uv run alembic revision --autogenerate -m "description"

# Apply migrations
uv run alembic upgrade head

# Rollback last migration
uv run alembic downgrade -1

# View migration history
uv run alembic history
```

### Running Tests
```bash
# Run all tests
uv run pytest

# Run with coverage
uv run pytest --cov=app

# Run specific test file
uv run pytest tests/test_tasks.py
```

## API Endpoints

### Public Endpoints
- `POST /auth/register` - Create new user account
- `POST /auth/login` - Authenticate and receive JWT token
- `GET /` - API information
- `GET /health` - Health check

### Protected Endpoints (require JWT in Authorization header)
- `GET /api/{user_id}/tasks` - Get all user's tasks
- `POST /api/{user_id}/tasks` - Create new task
- `GET /api/{user_id}/tasks/{task_id}` - Get specific task
- `PUT /api/{user_id}/tasks/{task_id}` - Update task
- `DELETE /api/{user_id}/tasks/{task_id}` - Delete task

### Authentication
All protected endpoints require JWT token in Authorization header:
```
Authorization: Bearer <your-jwt-token>
```

## Database Schema

### Users Table
```sql
CREATE TABLE users (
    id UUID PRIMARY KEY,
    email VARCHAR UNIQUE NOT NULL,
    password_hash VARCHAR NOT NULL,
    name VARCHAR,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);
```

### Tasks Table
```sql
CREATE TABLE tasks (
    id SERIAL PRIMARY KEY,
    user_id UUID NOT NULL REFERENCES users(id),
    title VARCHAR(200) NOT NULL,
    description TEXT,
    completed BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

CREATE INDEX idx_tasks_user_id ON tasks(user_id);
CREATE INDEX idx_tasks_completed ON tasks(completed);
```

## Environment Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `DATABASE_URL` | PostgreSQL connection string | `postgresql://user:pass@host/db` |
| `JWT_SECRET` | Secret key for JWT signing | `your-secret-key` |
| `CORS_ORIGINS` | Allowed frontend origins | `http://localhost:3000` |

## Deployment

### Railway / Render / Fly.io

1. Create new service
2. Connect GitHub repository
3. Set environment variables
4. Deploy `backend` directory
5. Run migrations: `uv run alembic upgrade head`

### Docker (Optional)
```dockerfile
FROM python:3.13-slim
WORKDIR /app
COPY . .
RUN pip install uv && uv sync
CMD ["uv", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

## Security Considerations

- Passwords are hashed with bcrypt before storage
- JWT tokens expire after 7 days
- CORS is configured to allow only specific origins
- All database queries use parameterized statements (SQLModel)
- User isolation enforced on all endpoints
- Environment variables used for secrets (never hardcoded)

## References

- [FastAPI Documentation](https://fastapi.tiangolo.com)
- [SQLModel Documentation](https://sqlmodel.tiangolo.com)
- [Alembic Documentation](https://alembic.sqlalchemy.org)
- [Neon PostgreSQL](https://neon.tech/docs)
- [Project Specification](../specs/phase-ii-web-app/spec.md)
- [Implementation Plan](../specs/phase-ii-web-app/plan.md)
