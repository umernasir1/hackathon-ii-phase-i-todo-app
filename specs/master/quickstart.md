# Quickstart Guide: Todo Console App (Phase I)

**Feature Branch**: `001-phase-i-console-app`
**Date**: 2025-12-17
**Version**: 1.0.0

## Overview

This is a simple command-line todo application built with Python 3.13+. Tasks are stored in memory only (not persisted between sessions). Perfect for quick task management during your work session.

---

## Prerequisites

Before you begin, ensure you have:

- **Python 3.13+** installed ([Download here](https://www.python.org/downloads/))
- **UV package manager** installed ([Installation guide](https://github.com/astral-sh/uv))

### Check Your Installation

```bash
# Check Python version
python --version
# Should output: Python 3.13.x or higher

# Check UV installation
uv --version
# Should output: uv x.x.x
```

### Installing UV (if not installed)

**Windows (PowerShell)**:
```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**macOS/Linux**:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/HackatonII.git
cd HackatonII
```

### 2. Initialize Python Project with UV

```bash
# Create virtual environment and install dependencies
uv venv
uv pip install -e .
```

**Note**: Since this project uses only Python standard library, no external dependencies are installed.

---

## Running the Application

### Start the Todo App

```bash
# Activate virtual environment (if not already activated)
# Windows
.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate

# Run the application
uv run python src/main.py
```

**Alternative (without activating venv)**:
```bash
uv run python src/main.py
```

You should see:

```
╔════════════════════════════════════════════════╗
║        Todo Console App - Phase I              ║
║  Type 'help' for available commands            ║
║  Type 'exit' to quit                           ║
╚════════════════════════════════════════════════╝

> _
```

---

## Usage Guide

### Basic Commands

#### 1. Add a New Task

```bash
# Add task with title only
> add Buy groceries

# Add task with title and description
> add Buy groceries - milk, eggs, bread

# Output:
✓ Task 1 added successfully
```

#### 2. View All Tasks

```bash
> list
# Alternative commands: view, show

# Output:
ID │ Status │ Title                    │ Description
───┼────────┼─────────────────────────┼────────────────────
1  │ ○      │ Buy groceries            │ milk, eggs, bread
2  │ ✓      │ Call mom                 │ Birthday wishes
3  │ ○      │ Finish report            │ Q4 summary

3 tasks total (1 completed, 2 pending)
```

**Legend**:
- `○` = Pending task
- `✓` = Completed task

#### 3. Mark Task as Complete

```bash
> complete 1
# Alternative commands: done 1

# Output:
✓ Task 1 marked as complete
```

#### 4. Mark Task as Incomplete

```bash
> uncomplete 1

# Output:
✓ Task 1 marked as incomplete
```

#### 5. Update Task Details

```bash
# Update title
> update 1 title Buy groceries and supplies

# Update description
> update 1 description Need milk, eggs, and bread

# Output:
✓ Task 1 updated successfully
```

#### 6. Delete a Task

```bash
> delete 1
# Alternative commands: remove 1

# Output:
✓ Task 1 deleted successfully
```

#### 7. Get Help

```bash
> help

# Shows all available commands with examples
```

#### 8. Exit the Application

```bash
> exit
# Alternative commands: quit

# Output:
⚠️  WARNING: Tasks are not saved. They will be lost when you exit.
Are you sure you want to exit? (yes/no): yes

Goodbye!
```

---

## Command Reference

| Command | Syntax | Description | Example |
|---------|--------|-------------|---------|
| **add** | `add <title>` or `add <title> - <description>` | Create new task | `add Buy groceries - milk, eggs` |
| **list** | `list` or `view` or `show` | Display all tasks | `list` |
| **complete** | `complete <id>` or `done <id>` | Mark task complete | `complete 1` |
| **uncomplete** | `uncomplete <id>` | Mark task incomplete | `uncomplete 1` |
| **update** | `update <id> title <new_title>` | Update task title | `update 1 title New title` |
|         | `update <id> description <new_desc>` | Update description | `update 1 description New desc` |
| **delete** | `delete <id>` or `remove <id>` | Delete task | `delete 1` |
| **help** | `help` | Show command help | `help` |
| **exit** | `exit` or `quit` | Exit application | `exit` |

---

## Example Session

Here's a complete example session:

```bash
> add Buy groceries
✓ Task 1 added successfully

> add Call mom - Birthday wishes
✓ Task 2 added successfully

> add Finish report - Q4 summary
✓ Task 3 added successfully

> list
ID │ Status │ Title                    │ Description
───┼────────┼─────────────────────────┼────────────────────
1  │ ○      │ Buy groceries            │
2  │ ○      │ Call mom                 │ Birthday wishes
3  │ ○      │ Finish report            │ Q4 summary

3 tasks total (0 completed, 3 pending)

> complete 2
✓ Task 2 marked as complete

> update 1 description milk, eggs, bread
✓ Task 1 updated successfully

> list
ID │ Status │ Title                    │ Description
───┼────────┼─────────────────────────┼────────────────────
1  │ ○      │ Buy groceries            │ milk, eggs, bread
2  │ ✓      │ Call mom                 │ Birthday wishes
3  │ ○      │ Finish report            │ Q4 summary

3 tasks total (1 completed, 2 pending)

> delete 3
✓ Task 3 deleted successfully

> list
ID │ Status │ Title                    │ Description
───┼────────┼─────────────────────────┼────────────────────
1  │ ○      │ Buy groceries            │ milk, eggs, bread
2  │ ✓      │ Call mom                 │ Birthday wishes

2 tasks total (1 completed, 1 pending)

> exit
⚠️  WARNING: Tasks are not saved. They will be lost when you exit.
Are you sure you want to exit? (yes/no): yes

Goodbye!
```

---

## Common Errors & Solutions

### Error: "Title is required"

**Cause**: You tried to add a task without a title or with only whitespace.

**Solution**: Provide a non-empty title:
```bash
> add Buy groceries
```

### Error: "Title must be 200 characters or less"

**Cause**: Task title exceeds 200 characters.

**Solution**: Shorten your title or move extra details to the description:
```bash
> add Buy groceries - milk, eggs, bread, cheese, yogurt, etc.
```

### Error: "Description must be 1000 characters or less"

**Cause**: Task description exceeds 1000 characters.

**Solution**: Shorten your description or split into multiple tasks.

### Error: "Task ID X not found"

**Cause**: You referenced a task ID that doesn't exist (deleted or never created).

**Solution**: Run `list` to see available task IDs:
```bash
> list
> complete 1  # Use existing ID
```

### Error: "Invalid command"

**Cause**: You entered a command that doesn't exist.

**Solution**: Type `help` to see all available commands:
```bash
> help
```

### Error: "Invalid task ID. Please enter a number."

**Cause**: You provided a non-numeric task ID.

**Solution**: Use a numeric ID:
```bash
> complete 1  # Correct
> complete abc  # Wrong
```

---

## Important Notes

### ⚠️ Data is NOT Saved

**This application stores tasks in memory only**. When you exit the app, all tasks are permanently lost.

**Why?**: Phase I of the hackathon requires in-memory storage only. Persistence (file or database) will be added in Phase II.

**Workaround**: Keep the app running during your work session, or manually save tasks elsewhere if needed.

### Performance Limits

- **Maximum tasks**: Designed to handle up to 1000 tasks efficiently
- **Response time**: All operations complete in < 100ms
- **Memory usage**: Minimal (each task ~1KB in memory)

### Validation Rules

- **Title**: 1-200 characters (required)
- **Description**: 0-1000 characters (optional)
- **Task ID**: Positive integer, auto-assigned, never reused

---

## Development & Testing

### Run Tests (Optional)

If you want to run the test suite:

```bash
# Install pytest (only dev dependency)
uv pip install pytest

# Run tests
pytest tests/

# Run with coverage
pytest --cov=src tests/
```

### Code Structure

```
HackatonII/
├── src/
│   ├── __init__.py
│   ├── models.py          # Task dataclass
│   ├── task_manager.py    # TaskManager (CRUD logic)
│   ├── cli.py             # CLI interface
│   └── main.py            # Entry point
├── tests/                 # Optional tests
│   ├── test_models.py
│   ├── test_task_manager.py
│   └── test_cli.py
├── specs/                 # Specification documents
├── pyproject.toml         # UV configuration
└── README.md
```

---

## Troubleshooting

### Python 3.13 Not Found

**Issue**: `python: command not found` or version < 3.13

**Solution**: Install Python 3.13+ from [python.org](https://www.python.org/downloads/)

### UV Not Found

**Issue**: `uv: command not found`

**Solution**: Install UV following the [installation guide](https://github.com/astral-sh/uv)

### Virtual Environment Issues

**Issue**: Module not found errors

**Solution**: Ensure you're in the virtual environment:
```bash
# Windows
.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate
```

### Application Won't Start

**Issue**: Errors when running `uv run python src/main.py`

**Solution**: Check that all files exist in the `src/` directory:
```bash
ls src/
# Should show: __init__.py, models.py, task_manager.py, cli.py, main.py
```

---

## Next Steps

### Phase II: Web Interface (Coming Soon)

Phase I is a console app. In Phase II, we'll add:
- Next.js 16+ frontend with React components
- FastAPI backend with RESTful API
- PostgreSQL database for persistence
- Better Auth for user authentication

Stay tuned for updates!

### Feedback & Issues

If you encounter bugs or have feature requests, please:
1. Check the [spec.md](./spec.md) for expected behavior
2. Review this quickstart guide for common errors
3. Open an issue on GitHub with detailed steps to reproduce

---

## FAQ

**Q: Can I save my tasks to a file?**
A: Not in Phase I. Persistence will be added in Phase II with a database.

**Q: Can multiple users use the app at the same time?**
A: No, this is a single-user console application. Multi-user support comes in Phase II.

**Q: Can I set due dates or priorities?**
A: Not in Phase I (Basic Level features only). These are Intermediate/Advanced Level features for later phases.

**Q: Can I search or filter tasks?**
A: Not in Phase I. Search/filter functionality is an Intermediate Level feature for Phase II.

**Q: Why does the app warn me when I exit?**
A: Because tasks are stored in memory only and will be lost. This is by design for Phase I.

**Q: Can I change the visual style (colors, symbols)?**
A: Not currently. The CLI output is standardized per the spec. Customization may come in future phases.

---

## Quick Reference Card

**Print this for easy reference!**

```
┌─────────────────────────────────────────────────┐
│         Todo Console App - Quick Ref            │
├─────────────────────────────────────────────────┤
│ add <title>              Add new task           │
│ list                     View all tasks         │
│ complete <id>            Mark complete          │
│ uncomplete <id>          Mark incomplete        │
│ update <id> title <text> Update title           │
│ update <id> desc <text>  Update description     │
│ delete <id>              Delete task            │
│ help                     Show help              │
│ exit                     Quit (data not saved!) │
└─────────────────────────────────────────────────┘
```

---

**Version**: 1.0.0 | **Last Updated**: 2025-12-17 | **Phase**: Phase I

For detailed technical documentation, see:
- [spec.md](./spec.md) - Feature specification
- [plan.md](./plan.md) - Implementation plan
- [data-model.md](./data-model.md) - Data model details
- [research.md](./research.md) - Technology decisions
