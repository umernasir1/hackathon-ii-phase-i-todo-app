"""Task management business logic.

This module contains the TaskManager class that handles CRUD operations
for tasks stored in memory.
"""

from datetime import datetime
from typing import Optional

from models import Task


class TaskManager:
    """Manages in-memory collection of tasks.

    Attributes:
        tasks: Dictionary mapping task IDs to Task objects
        next_id: Counter for auto-incrementing task IDs
    """

    def __init__(self) -> None:
        """Initialize TaskManager with empty storage."""
        self.tasks: dict[int, Task] = {}
        self.next_id: int = 1

    def add_task(self, title: str, description: str = "") -> Task:
        """Create a new task and store it in memory.

        Args:
            title: Task title (1-200 chars, required)
            description: Optional description (0-1000 chars, default empty)

        Returns:
            The newly created Task object

        Raises:
            ValueError: If title/description validation fails
        """
        now = datetime.now()
        task = Task(
            id=self.next_id,
            title=title,
            description=description,
            completed=False,
            created_at=now,
            updated_at=now,
        )
        self.tasks[self.next_id] = task
        self.next_id += 1
        return task

    def get_all_tasks(self) -> list[Task]:
        """Retrieve all tasks sorted by ID.

        Returns:
            List of all Task objects, sorted by ID ascending (empty list if no tasks)
        """
        return sorted(self.tasks.values(), key=lambda t: t.id)

    def get_task(self, task_id: int) -> Optional[Task]:
        """Retrieve a single task by ID.

        Args:
            task_id: The task ID to retrieve

        Returns:
            Task object if found, None if not found
        """
        return self.tasks.get(task_id)

    def update_task(
        self, task_id: int, title: Optional[str] = None, description: Optional[str] = None
    ) -> Task:
        """Update a task's title and/or description.

        Args:
            task_id: The task ID to update
            title: New title (optional, None = no change)
            description: New description (optional, None = no change)

        Returns:
            The updated Task object

        Raises:
            ValueError: If task_id not found or if title/description validation fails
        """
        task = self.get_task(task_id)
        if task is None:
            raise ValueError(f"Task ID {task_id} not found")

        if title is not None:
            task.update_title(title)

        if description is not None:
            task.update_description(description)

        return task

    def complete_task(self, task_id: int, completed: bool = True) -> Task:
        """Mark a task as complete or incomplete.

        Args:
            task_id: The task ID to update
            completed: True for complete, False for incomplete (default True)

        Returns:
            The updated Task object

        Raises:
            ValueError: If task_id not found
        """
        task = self.get_task(task_id)
        if task is None:
            raise ValueError(f"Task ID {task_id} not found")

        if completed:
            task.mark_complete()
        else:
            task.mark_incomplete()

        return task

    def delete_task(self, task_id: int) -> Task:
        """Delete a task from storage.

        Args:
            task_id: The task ID to delete

        Returns:
            The deleted Task object

        Raises:
            ValueError: If task_id not found

        Note:
            IDs are not reused - next_id continues incrementing
        """
        task = self.get_task(task_id)
        if task is None:
            raise ValueError(f"Task ID {task_id} not found")

        del self.tasks[task_id]
        return task
