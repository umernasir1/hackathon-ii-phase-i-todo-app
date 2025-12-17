"""Data models for the Todo application.

This module contains the Task entity with validation logic.
"""

from dataclasses import dataclass
from datetime import datetime


@dataclass
class Task:
    """Represents a todo task with validation.

    Attributes:
        id: Unique integer identifier (auto-assigned by TaskManager)
        title: Task title (1-200 characters, required)
        description: Optional detailed description (0-1000 characters)
        completed: Completion status (True/False)
        created_at: Timestamp when task was created
        updated_at: Timestamp when task was last modified
    """

    id: int
    title: str
    description: str
    completed: bool
    created_at: datetime
    updated_at: datetime

    def __post_init__(self) -> None:
        """Validate task fields after initialization.

        Raises:
            ValueError: If validation fails (empty title, title/description too long)
        """
        # Validate title
        if not self.title or len(self.title.strip()) < 1:
            raise ValueError("Title is required")

        if len(self.title) > 200:
            raise ValueError("Title must be 200 characters or less")

        # Validate description
        if len(self.description) > 1000:
            raise ValueError("Description must be 1000 characters or less")

        # Strip whitespace from title and description (normalize)
        self.title = self.title.strip()
        self.description = self.description.strip()

    def mark_complete(self) -> None:
        """Mark this task as complete and update timestamp."""
        self.completed = True
        self.updated_at = datetime.now()

    def mark_incomplete(self) -> None:
        """Mark this task as incomplete and update timestamp."""
        self.completed = False
        self.updated_at = datetime.now()

    def update_title(self, new_title: str) -> None:
        """Update task title with validation.

        Args:
            new_title: New title for the task

        Raises:
            ValueError: If title is empty or too long
        """
        if not new_title or len(new_title.strip()) < 1:
            raise ValueError("Title is required")

        if len(new_title) > 200:
            raise ValueError("Title must be 200 characters or less")

        self.title = new_title.strip()
        self.updated_at = datetime.now()

    def update_description(self, new_description: str) -> None:
        """Update task description with validation.

        Args:
            new_description: New description for the task

        Raises:
            ValueError: If description is too long
        """
        if len(new_description) > 1000:
            raise ValueError("Description must be 1000 characters or less")

        self.description = new_description.strip()
        self.updated_at = datetime.now()

    def __str__(self) -> str:
        """String representation for display."""
        status = "✓" if self.completed else "○"
        return f"[{self.id}] {status} {self.title}"
