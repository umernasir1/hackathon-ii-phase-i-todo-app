from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from contextlib import asynccontextmanager

from app.database import create_db_and_tables
from app.routers import auth, tasks
from app.config import settings

# Load environment variables
load_dotenv()


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Lifespan event handler for database initialization"""
    # Startup: Create database tables
    create_db_and_tables()
    yield
    # Shutdown: cleanup if needed


app = FastAPI(
    title="Todo API",
    description="Backend API for Phase II Todo Application",
    version="1.0.0",
    lifespan=lifespan
)

# CORS configuration for Next.js frontend
origins = [
    "http://localhost:3000",  # Next.js dev server
    "https://localhost:3000",
]

# Add FRONTEND_URL if configured
if settings.frontend_url and settings.frontend_url.strip():
    origins.append(settings.frontend_url)

# Also add common Vercel patterns for preview deployments
origins.extend([
    "https://hackathon-ii-todo-app.vercel.app",
    "https://hackathon-ii-todo-app-git-main-umernasir1s-projects.vercel.app",
])

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router)
app.include_router(tasks.router)


@app.get("/")
def read_root():
    return {
        "message": "Todo API is running",
        "version": "1.0.0",
        "docs": "/docs"
    }


@app.get("/health")
def health_check():
    return {"status": "healthy"}
