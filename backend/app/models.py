from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from datetime import datetime


class User(SQLModel, table=True):
    """User model for authentication and task ownership"""

    __tablename__ = "users"

    id: Optional[int] = Field(default=None, primary_key=True)
    email: str = Field(unique=True, index=True, max_length=255)
    password_hash: str = Field(max_length=255)
    created_at: datetime = Field(default_factory=datetime.utcnow)

    # Relationship
    tasks: List["Task"] = Relationship(
        back_populates="user",
        sa_relationship_kwargs={"cascade": "all, delete-orphan"}
    )


class Task(SQLModel, table=True):
    """Task model for todo items"""

    __tablename__ = "tasks"

    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="users.id", index=True)
    title: str = Field(max_length=255)
    description: Optional[str] = Field(default=None, max_length=1000)
    completed: bool = Field(default=False)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    # Relationship
    user: Optional[User] = Relationship(back_populates="tasks")


# Pydantic models for API requests/responses
class UserCreate(SQLModel):
    """Schema for user registration"""
    email: str
    password: str


class UserLogin(SQLModel):
    """Schema for user login"""
    email: str
    password: str


class UserResponse(SQLModel):
    """Schema for user response (without password)"""
    id: int
    email: str
    created_at: datetime


class Token(SQLModel):
    """Schema for JWT token response"""
    access_token: str
    token_type: str = "bearer"
    user: UserResponse


class TaskCreate(SQLModel):
    """Schema for creating a task"""
    title: str
    description: Optional[str] = None


class TaskUpdate(SQLModel):
    """Schema for updating a task"""
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None


class TaskResponse(SQLModel):
    """Schema for task response"""
    id: int
    user_id: int
    title: str
    description: Optional[str]
    completed: bool
    created_at: datetime
    updated_at: datetime


class TaskListResponse(SQLModel):
    """Schema for task list response with summary"""
    tasks: List[TaskResponse]
    total: int
    completed: int
    pending: int
