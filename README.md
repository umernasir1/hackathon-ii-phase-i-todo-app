# Hackathon II - Todo Application

![Python Version](https://img.shields.io/badge/python-3.11+-blue.svg)
![Next.js](https://img.shields.io/badge/Next.js-16-black.svg)
![License](https://img.shields.io/badge/license-Educational-green.svg)
![Status](https://img.shields.io/badge/status-Phase%20II%20Complete-success.svg)

A full-stack todo application demonstrating spec-driven development. Phase I is a Python console app with in-memory storage. Phase II is a full-stack web application with Next.js, FastAPI, and PostgreSQL.

## 🚀 Quick Start

### Phase I - Console App (Completed)
```bash
cd src
python main.py
```

### Phase II - Web Application (Completed)

**Prerequisites**:
- Python 3.11+
- Node.js 18+
- Neon PostgreSQL account (free tier)

**Backend Setup**:
```bash
cd backend
pip install -r requirements.txt
# Configure .env with your Neon database URL
python -m alembic upgrade head
python -m uvicorn main:app --reload --port 8000
```

**Frontend Setup**:
```bash
cd frontend
npm install
npm run dev
```

Access the app at `http://localhost:3000`

## 📋 Project Structure

```
HackatonII/
├── src/                  # Phase I: Console app (Python)
│   ├── models.py
│   ├── task_manager.py
│   ├── cli.py
│   └── main.py
├── backend/              # Phase II: FastAPI backend
│   ├── app/
│   │   ├── models.py          # SQLModel database models
│   │   ├── database.py        # Database connection
│   │   ├── auth.py            # JWT authentication
│   │   ├── config.py          # Settings
│   │   └── routers/
│   │       ├── auth.py        # /auth/register, /auth/login
│   │       └── tasks.py       # /api/{user_id}/tasks CRUD
│   ├── alembic/               # Database migrations
│   ├── main.py                # FastAPI app entry point
│   ├── requirements.txt
│   └── README.md
├── frontend/             # Phase II: Next.js frontend
│   ├── app/
│   │   ├── layout.tsx
│   │   ├── page.tsx           # Landing page
│   │   ├── login/             # Login page
│   │   ├── signup/            # Registration page
│   │   └── dashboard/         # Main todo dashboard
│   ├── lib/
│   │   ├── types.ts           # TypeScript types
│   │   ├── api.ts             # Backend API client
│   │   └── auth-context.tsx   # Authentication context
│   ├── package.json
│   └── README.md
└── specs/                # Specification documents
    ├── master/                # Phase I specs
    └── phase-ii-web-app/      # Phase II specs
        ├── spec.md
        ├── plan.md
        └── tasks.md
```

## ✨ Features

### Phase I - Console App
✅ **5 Basic Level Features**:
1. Add tasks with title and description
2. View all tasks in formatted table
3. Mark tasks as complete/incomplete
4. Update task title and description
5. Delete tasks

### Phase II - Web Application
✅ **All Phase I features** migrated to web interface
✅ **User Authentication**: Register and login with email/password
✅ **Persistent Storage**: PostgreSQL database via Neon
✅ **Responsive Design**: Works on mobile, tablet, and desktop
✅ **RESTful API**: FastAPI backend with full CRUD operations
✅ **Type Safety**: TypeScript frontend, Python type hints
✅ **JWT Tokens**: Secure authentication with 7-day expiry
✅ **Real-time Updates**: Instant UI feedback for all operations

## 🏗️ Technology Stack

### Phase II Stack
- **Frontend**: Next.js 16+ (App Router), React 19, TypeScript, Tailwind CSS
- **Backend**: FastAPI, Python 3.11+, SQLModel, Pydantic
- **Database**: Neon PostgreSQL (serverless)
- **Authentication**: JWT tokens with bcrypt password hashing
- **API**: RESTful endpoints with OpenAPI documentation
- **Development**: UV package manager (Python), npm (Node.js)

## 📚 API Documentation

### Public Endpoints
- `POST /auth/register` - Create new user account
- `POST /auth/login` - Authenticate and receive JWT token
- `GET /health` - Health check

### Protected Endpoints (require JWT)
- `GET /api/{user_id}/tasks` - Get all user's tasks
- `POST /api/{user_id}/tasks` - Create new task
- `GET /api/{user_id}/tasks/{task_id}` - Get specific task
- `PUT /api/{user_id}/tasks/{task_id}` - Update task
- `DELETE /api/{user_id}/tasks/{task_id}` - Delete task

Interactive API docs: `http://localhost:8000/docs`

## 🔧 Configuration

### Backend (.env)
```bash
DATABASE_URL=postgresql://user:password@host/database?sslmode=require
JWT_SECRET=your-super-secret-jwt-key-change-this
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_DAYS=7
FRONTEND_URL=http://localhost:3000
```

### Frontend (.env.local)
```bash
NEXT_PUBLIC_API_URL=http://localhost:8000
```

## 🗄️ Database Schema

### Users Table
```sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT NOW()
);
```

### Tasks Table
```sql
CREATE TABLE tasks (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    completed BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

CREATE INDEX idx_tasks_user_id ON tasks(user_id);
```

## 🚦 Getting Started - Detailed Guide

### Step 1: Clone Repository
```bash
git clone https://github.com/umernasir1/hackathon-ii-todo-app.git
cd HackatonII
```

### Step 2: Set Up Neon Database
1. Go to [https://console.neon.tech](https://console.neon.tech)
2. Create new project: "hackathon-todo-app"
3. Copy connection string
4. Paste into `backend/.env` as `DATABASE_URL`

### Step 3: Install Backend Dependencies
```bash
cd backend
pip install -r requirements.txt
```

### Step 4: Run Database Migrations
```bash
cd backend
python -m alembic upgrade head
```

### Step 5: Start Backend Server
```bash
cd backend
python -m uvicorn main:app --reload --port 8000
```

### Step 6: Install Frontend Dependencies
```bash
cd frontend
npm install
```

### Step 7: Start Frontend Server
```bash
cd frontend
npm run dev
```

### Step 8: Access Application
Open browser to `http://localhost:3000`

## 🧪 Testing

### Backend
```bash
cd backend
# Start backend server
python -m uvicorn main:app --reload --port 8000

# In another terminal, test endpoints
curl http://localhost:8000/health
curl -X POST http://localhost:8000/auth/register \
  -H "Content-Type: application/json" \
  -d '{"email":"test@example.com","password":"test123"}'
```

### Frontend
```bash
cd frontend
npm run build  # Check for TypeScript errors
npm run dev    # Test in browser
```

## 📱 User Guide

### Registration
1. Click "Sign Up" on landing page
2. Enter email and password (min 6 characters)
3. Click "Sign up" - you'll be automatically logged in

### Login
1. Click "Login" on landing page
2. Enter your email and password
3. Click "Sign in"

### Managing Tasks
1. **Add Task**: Fill in title and optional description, click "Add Task"
2. **View Tasks**: All tasks displayed in list with status
3. **Complete Task**: Click checkbox to toggle completion
4. **Edit Task**: Click "Edit", modify fields, click "Save"
5. **Delete Task**: Click "Delete" and confirm

### Logout
Click "Logout" button in header

## 🐛 Troubleshooting

### Backend Issues

**Cannot connect to database**:
- Verify `DATABASE_URL` in `.env` is correct
- Check Neon database is active
- Ensure `?sslmode=require` is in connection string

**Alembic migration errors**:
```bash
# Reset migrations (development only)
cd backend
python -m alembic downgrade base
python -m alembic upgrade head
```

**CORS errors**:
- Verify `FRONTEND_URL` in backend `.env` matches frontend URL
- Check backend server is running on port 8000

### Frontend Issues

**Cannot connect to backend**:
- Verify `NEXT_PUBLIC_API_URL` in `.env.local` is correct
- Check backend server is running
- Open `http://localhost:8000/docs` to verify backend

**TypeScript errors**:
```bash
cd frontend
npm run build  # Check for errors
```

**Authentication not working**:
- Clear browser localStorage (Application > Local Storage > Clear)
- Try logging in again

## 📖 Development Workflow

This project follows spec-driven development (SDD):

1. **Specification** (`specs/.../spec.md`) - User stories and requirements
2. **Planning** (`specs/.../plan.md`) - Architecture and technical decisions
3. **Tasks** (`specs/.../tasks.md`) - Atomic task breakdown
4. **Implementation** - Code development
5. **Testing** - Validation of features

See individual `CLAUDE.md` files in `backend/` and `frontend/` for detailed development guidelines.

## 🎯 Project Milestones

- ✅ Phase I: Console App (Dec 10, 2025)
- ✅ Phase II Specification (Dec 18, 2025)
- ✅ Phase II Implementation Plan (Dec 18, 2025)
- ✅ Phase II Backend Setup (Dec 18, 2025)
- ✅ Phase II Frontend Setup (Dec 18, 2025)
- ✅ Phase II Authentication System (Dec 18, 2025)
- ✅ Phase II Full Implementation (Dec 18, 2025)
- ✅ Phase II Testing & Validation (Dec 21, 2025)
- ⚡ Phase II Ready for Deployment

## 📡 Deployment Status

### Ready for Production
The application is fully implemented, tested, and ready to deploy:

**Backend:**
- ✅ FastAPI application complete
- ✅ Database migrations configured
- ✅ JWT authentication implemented
- ✅ All API endpoints tested
- ✅ Deployment configs ready (Procfile, railway.toml, runtime.txt)
- 🔜 Deploy to: Railway / Render / Fly.io

**Frontend:**
- ✅ Next.js 16 application complete
- ✅ All pages implemented
- ✅ Authentication flow working
- ✅ Production build tested
- ✅ Deployment config ready (vercel.json)
- 🔜 Deploy to: Vercel

**Database:**
- ✅ Neon PostgreSQL configured
- ✅ Schema migrations ready
- ✅ Connection tested

### Deployment Instructions
See [DEPLOYMENT.md](./DEPLOYMENT.md) for step-by-step deployment guide.

### Testing
See [TESTING_CHECKLIST.md](./TESTING_CHECKLIST.md) for comprehensive testing checklist.

## 📄 License

This project is part of Hackathon II educational assignment.

## 🙏 Acknowledgments

- Built with Claude Code using spec-driven development
- Follows clean architecture principles
- Implements PIAIC Hackathon II requirements

---

**Version**: 2.0.0 | **Phase**: Phase II Complete - Ready for Deployment | **Date**: 2025-12-21
"" 
