# Data Model: Todo Console App (Phase I)

**Feature Branch**: `001-phase-i-console-app`
**Date**: 2025-12-17
**Phase**: Phase 1 (Design & Contracts)

## Overview

This document defines the data model for the in-memory todo console application. The model consists of a single entity (Task) and a manager class (TaskManager) that handles business logic and storage.

---

## Entity: Task

### Description

Represents a single todo item with a title, optional description, completion status, and timestamps.

### Attributes

| Attribute | Type | Required | Constraints | Default | Description |
|-----------|------|----------|-------------|---------|-------------|
| `id` | `int` | Yes | Positive integer, unique | Auto-generated | Unique identifier for the task |
| `title` | `str` | Yes | 1-200 characters | None | Task title (main description) |
| `description` | `str` | No | 0-1000 characters | Empty string | Optional detailed description |
| `completed` | `bool` | Yes | True or False | `False` | Completion status |
| `created_at` | `datetime` | Yes | Valid datetime | Auto-generated | Timestamp when task was created |
| `updated_at` | `datetime` | Yes | Valid datetime | Auto-updated | Timestamp when task was last modified |

### Python Implementation

```python
from dataclasses import dataclass
from datetime import datetime

@dataclass
class Task:
    """Represents a todo task with validation."""

    id: int
    title: str
    description: str
    completed: bool
    created_at: datetime
    updated_at: datetime

    def __post_init__(self):
        """Validate task fields after initialization."""
        # Validate title
        if not self.title or len(self.title.strip()) < 1:
            raise ValueError("Title is required")

        if len(self.title) > 200:
            raise ValueError("Title must be 200 characters or less")

        # Validate description
        if len(self.description) > 1000:
            raise ValueError("Description must be 1000 characters or less")

        # Strip whitespace from title (normalize)
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
        """Update task title with validation."""
        if not new_title or len(new_title.strip()) < 1:
            raise ValueError("Title is required")

        if len(new_title) > 200:
            raise ValueError("Title must be 200 characters or less")

        self.title = new_title.strip()
        self.updated_at = datetime.now()

    def update_description(self, new_description: str) -> None:
        """Update task description with validation."""
        if len(new_description) > 1000:
            raise ValueError("Description must be 1000 characters or less")

        self.description = new_description.strip()
        self.updated_at = datetime.now()

    def __str__(self) -> str:
        """String representation for display."""
        status = "✓" if self.completed else "○"
        return f"[{self.id}] {status} {self.title}"
```

### Validation Rules

#### Title Validation
- **Required**: Title cannot be empty or whitespace-only
- **Length**: 1-200 characters after stripping whitespace
- **Normalization**: Leading/trailing whitespace is automatically removed
- **Error**: Raises `ValueError` with descriptive message

#### Description Validation
- **Optional**: Can be empty string
- **Length**: 0-1000 characters after stripping whitespace
- **Normalization**: Leading/trailing whitespace is automatically removed
- **Error**: Raises `ValueError` if too long

#### ID Validation
- **Uniqueness**: Enforced by TaskManager (not in Task itself)
- **Auto-increment**: TaskManager assigns IDs sequentially
- **Immutable**: IDs should never change after creation

#### Timestamp Validation
- **Auto-set**: `created_at` set on task creation
- **Auto-update**: `updated_at` set on any modification
- **Immutable created_at**: Should not change after creation
- **Type**: Python `datetime` objects

### Invariants

1. **Title is never empty**: After validation, title always has at least 1 non-whitespace character
2. **Timestamps are ordered**: `created_at` ≤ `updated_at` always
3. **Boolean completion**: `completed` is always True or False (never None)
4. **ID is positive**: ID is always > 0

---

## Manager Class: TaskManager

### Description

Handles business logic for task management, including CRUD operations, validation, and in-memory storage.

### Storage Structure

```python
class TaskManager:
    """Manages in-memory collection of tasks."""

    def __init__(self):
        self.tasks: dict[int, Task] = {}  # ID → Task mapping
        self.next_id: int = 1              # Auto-increment counter
```

**Why Dict?**:
- O(1) lookup by ID
- Natural fit for CRUD operations
- Efficient for up to 1000 tasks

### Public Interface

#### add_task(title: str, description: str = "") -> Task

**Purpose**: Create a new task and store it in memory.

**Parameters**:
- `title` (str): Task title (1-200 chars, required)
- `description` (str): Optional description (0-1000 chars, default empty)

**Returns**: The newly created `Task` object

**Raises**:
- `ValueError`: If title/description validation fails

**Behavior**:
1. Validate title and description (via Task dataclass)
2. Assign next available ID
3. Set `created_at` and `updated_at` to current timestamp
4. Set `completed = False`
5. Store in `self.tasks` dict
6. Increment `self.next_id`
7. Return the created task

**Example**:
```python
task = manager.add_task("Buy groceries", "milk, eggs, bread")
# Returns: Task(id=1, title="Buy groceries", description="milk, eggs, bread", ...)
```

---

#### get_all_tasks() -> list[Task]

**Purpose**: Retrieve all tasks sorted by ID.

**Parameters**: None

**Returns**: List of all `Task` objects, sorted by ID ascending

**Raises**: None

**Behavior**:
1. Get all tasks from `self.tasks.values()`
2. Sort by ID ascending
3. Return list (empty list if no tasks)

**Example**:
```python
tasks = manager.get_all_tasks()
# Returns: [Task(id=1, ...), Task(id=2, ...), Task(id=3, ...)]
```

---

#### get_task(task_id: int) -> Task | None

**Purpose**: Retrieve a single task by ID.

**Parameters**:
- `task_id` (int): The task ID to retrieve

**Returns**: `Task` object if found, `None` if not found

**Raises**: None (returns None instead)

**Behavior**:
1. Look up task in `self.tasks` dict
2. Return task if found, None otherwise

**Example**:
```python
task = manager.get_task(1)
# Returns: Task(id=1, ...) or None
```

---

#### update_task(task_id: int, title: str | None = None, description: str | None = None) -> Task

**Purpose**: Update a task's title and/or description.

**Parameters**:
- `task_id` (int): The task ID to update
- `title` (str | None): New title (optional, None = no change)
- `description` (str | None): New description (optional, None = no change)

**Returns**: The updated `Task` object

**Raises**:
- `ValueError`: If task_id not found
- `ValueError`: If title/description validation fails

**Behavior**:
1. Look up task by ID (raise if not found)
2. If title provided, update with validation
3. If description provided, update with validation
4. Update `updated_at` timestamp
5. Return updated task

**Example**:
```python
task = manager.update_task(1, title="Buy groceries and supplies")
# Returns: Task(id=1, title="Buy groceries and supplies", ...)
```

---

#### complete_task(task_id: int, completed: bool = True) -> Task

**Purpose**: Mark a task as complete or incomplete.

**Parameters**:
- `task_id` (int): The task ID to update
- `completed` (bool): True for complete, False for incomplete (default True)

**Returns**: The updated `Task` object

**Raises**:
- `ValueError`: If task_id not found

**Behavior**:
1. Look up task by ID (raise if not found)
2. Set `completed` status
3. Update `updated_at` timestamp
4. Return updated task

**Example**:
```python
task = manager.complete_task(1)  # Mark complete
# Returns: Task(id=1, completed=True, ...)

task = manager.complete_task(1, completed=False)  # Mark incomplete
# Returns: Task(id=1, completed=False, ...)
```

---

#### delete_task(task_id: int) -> Task

**Purpose**: Delete a task from storage.

**Parameters**:
- `task_id` (int): The task ID to delete

**Returns**: The deleted `Task` object

**Raises**:
- `ValueError`: If task_id not found

**Behavior**:
1. Look up task by ID (raise if not found)
2. Remove from `self.tasks` dict
3. Return deleted task (for confirmation)
4. **Note**: Do NOT reuse the ID (keep incrementing `next_id`)

**Example**:
```python
task = manager.delete_task(2)
# Returns: Task(id=2, ...) (now deleted from storage)
```

---

### Error Messages

All error messages should be user-friendly and actionable:

| Error Condition | Error Message |
|-----------------|---------------|
| Empty title | `"Title is required"` |
| Title too long | `"Title must be 200 characters or less"` |
| Description too long | `"Description must be 1000 characters or less"` |
| Task not found | `"Task ID {task_id} not found"` |
| Invalid ID type | `"Invalid task ID. Please enter a number."` |

---

## Data Flow Diagrams

### Add Task Flow

```
User Input: "add Buy groceries - milk, eggs"
         ↓
    CLI.parse_command()
         ↓
    TaskManager.add_task("Buy groceries", "milk, eggs")
         ↓
    Task.__init__() + __post_init__()
         ↓
    Validation (title length, description length)
         ↓
    Store in tasks dict: {1: Task(...)}
         ↓
    Return Task object to CLI
         ↓
    CLI.display_success("Task 1 added successfully")
```

### Update Task Flow

```
User Input: "update 1 title Buy groceries and supplies"
         ↓
    CLI.parse_command()
         ↓
    TaskManager.update_task(1, title="Buy groceries and supplies")
         ↓
    Lookup task in dict (raise if not found)
         ↓
    Task.update_title("Buy groceries and supplies")
         ↓
    Validation (title length)
         ↓
    Update task.title and task.updated_at
         ↓
    Return Task object to CLI
         ↓
    CLI.display_success("Task 1 updated successfully")
```

### Complete Task Flow

```
User Input: "complete 1"
         ↓
    CLI.parse_command()
         ↓
    TaskManager.complete_task(1)
         ↓
    Lookup task in dict (raise if not found)
         ↓
    Task.mark_complete()
         ↓
    Update task.completed = True
    Update task.updated_at
         ↓
    Return Task object to CLI
         ↓
    CLI.display_success("Task 1 marked as complete")
```

---

## Test Scenarios

### Task Entity Tests

1. **Valid Task Creation**
   - Input: `Task(1, "Buy groceries", "", False, now, now)`
   - Expected: Task created successfully

2. **Empty Title Validation**
   - Input: `Task(1, "", "", False, now, now)`
   - Expected: Raises `ValueError("Title is required")`

3. **Title Too Long**
   - Input: `Task(1, "x" * 201, "", False, now, now)`
   - Expected: Raises `ValueError("Title must be 200 characters or less")`

4. **Description Too Long**
   - Input: `Task(1, "Title", "x" * 1001, False, now, now)`
   - Expected: Raises `ValueError("Description must be 1000 characters or less")`

5. **Whitespace Normalization**
   - Input: `Task(1, "  Title  ", "  Desc  ", False, now, now)`
   - Expected: `task.title == "Title"`, `task.description == "Desc"`

### TaskManager Tests

1. **Add First Task**
   - Input: `add_task("Buy groceries")`
   - Expected: Task with ID 1 created, stored in dict

2. **Add Multiple Tasks**
   - Input: Add 3 tasks
   - Expected: IDs 1, 2, 3 assigned sequentially

3. **Get All Tasks (Empty)**
   - Input: `get_all_tasks()` with no tasks
   - Expected: Returns empty list `[]`

4. **Get All Tasks (Multiple)**
   - Input: Add 3 tasks, call `get_all_tasks()`
   - Expected: Returns list of 3 tasks sorted by ID

5. **Get Task by ID (Exists)**
   - Input: `get_task(1)` where task 1 exists
   - Expected: Returns Task object

6. **Get Task by ID (Not Found)**
   - Input: `get_task(99)` where task 99 doesn't exist
   - Expected: Returns `None`

7. **Update Task Title**
   - Input: `update_task(1, title="New title")`
   - Expected: Task 1 title updated, `updated_at` changed

8. **Update Task Description**
   - Input: `update_task(1, description="New description")`
   - Expected: Task 1 description updated, `updated_at` changed

9. **Update Non-Existent Task**
   - Input: `update_task(99, title="Title")`
   - Expected: Raises `ValueError("Task ID 99 not found")`

10. **Complete Task**
    - Input: `complete_task(1)`
    - Expected: Task 1 `completed = True`, `updated_at` changed

11. **Delete Task**
    - Input: Add task 1, delete task 1
    - Expected: Task removed from dict, ID 1 not reused

12. **Delete Non-Existent Task**
    - Input: `delete_task(99)`
    - Expected: Raises `ValueError("Task ID 99 not found")`

---

## Performance Characteristics

| Operation | Time Complexity | Space Complexity | Notes |
|-----------|-----------------|------------------|-------|
| add_task | O(1) | O(1) | Dict insertion |
| get_all_tasks | O(n log n) | O(n) | Sorting by ID |
| get_task | O(1) | O(1) | Dict lookup |
| update_task | O(1) | O(1) | Dict lookup + update |
| complete_task | O(1) | O(1) | Dict lookup + update |
| delete_task | O(1) | O(1) | Dict deletion |

**Notes**:
- n = number of tasks (max 1000 for Phase I)
- All operations meet < 100ms requirement
- Sorting in get_all_tasks is O(n log n) but negligible for 1000 tasks

---

## Constitution Compliance

| Principle | Implementation |
|-----------|----------------|
| **Type Safety First** | All methods use type hints (`int`, `str`, `bool`, `datetime`, `dict[int, Task]`, `list[Task]`) |
| **Simplicity & Pragmatism** | No over-engineering: simple dict storage, straightforward CRUD methods |
| **Observability** | Clear error messages with context (`"Task ID {task_id} not found"`) |
| **Versioning** | Data model is v1.0.0, compatible with all Phase I requirements |

---

## Next Steps

✅ Phase 1 Data Model Complete

**Remaining Phase 1 Artifacts**:
- Create `quickstart.md` - Installation and usage instructions

**Phase 2**:
- Run `/sp.tasks` to generate actionable task breakdown from this data model

---

**Related Documents**:
- [spec.md](./spec.md) - Feature requirements
- [plan.md](./plan.md) - Implementation plan
- [research.md](./research.md) - Technology decisions
