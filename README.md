# Todo In-Memory Python Console App (Phase I)

A command-line todo application built with Python 3.13+ that stores tasks in memory. Part of Hackathon II project demonstrating spec-driven development with Claude Code.

## Features

✅ **5 Basic Level Features Implemented**:
1. **Add Tasks**: Create tasks with title and optional description
2. **View Tasks**: Display all tasks in formatted table with status indicators
3. **Mark Complete**: Toggle task completion status
4. **Update Tasks**: Edit task titles and descriptions
5. **Delete Tasks**: Remove tasks from the list

## Prerequisites

- Python 3.13+ ([Download](https://www.python.org/downloads/))
- UV package manager ([Installation guide](https://github.com/astral-sh/uv))

### Check Your Installation

```bash
python --version  # Should be 3.13.x or higher
uv --version      # Should show uv version
```

### Installing UV

**Windows (PowerShell)**:
```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**macOS/Linux**:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/HackatonII.git
cd HackatonII

# Create virtual environment (UV handles this automatically)
uv venv

# Run the application
uv run python src/main.py
```

## Usage

### Starting the App

```bash
uv run python src/main.py
```

You'll see:
```
╔════════════════════════════════════════════════╗
║        Todo Console App - Phase I              ║
║  Type 'help' for available commands            ║
║  Type 'exit' to quit                           ║
╚════════════════════════════════════════════════╝

> _
```

### Commands

**Add Tasks**:
```bash
> add Buy groceries
✓ Task 1 added successfully

> add Call mom - Birthday wishes
✓ Task 2 added successfully
```

**View Tasks**:
```bash
> list
ID │ Status │ Title                    │ Description
───┼────────┼──────────────────────────┼────────────────────
1  │ ○      │ Buy groceries            │
2  │ ○      │ Call mom                 │ Birthday wishes

2 tasks total (0 completed, 2 pending)
```

**Mark Complete**:
```bash
> complete 1
✓ Task 1 marked as complete

> uncomplete 1
✓ Task 1 marked as incomplete
```

**Update Tasks**:
```bash
> update 1 title Buy groceries and supplies
✓ Task 1 updated successfully

> update 1 description milk, eggs, bread
✓ Task 1 updated successfully
```

**Delete Tasks**:
```bash
> delete 2
✓ Task 2 deleted successfully
```

**Get Help**:
```bash
> help
# Shows all available commands with examples
```

**Exit**:
```bash
> exit
⚠️  WARNING: Tasks are not saved. They will be lost when you exit.
Are you sure you want to exit? (yes/no): yes
Goodbye!
```

## Command Reference

| Command | Description | Example |
|---------|-------------|---------|
| `add <title>` | Add task with title only | `add Buy groceries` |
| `add <title> - <description>` | Add task with description | `add Buy groceries - milk, eggs` |
| `list`, `view`, `show` | Display all tasks | `list` |
| `complete <id>`, `done <id>` | Mark task as complete | `complete 1` |
| `uncomplete <id>` | Mark task as incomplete | `uncomplete 1` |
| `update <id> title <text>` | Update task title | `update 1 title New title` |
| `update <id> description <text>` | Update description | `update 1 description New desc` |
| `delete <id>`, `remove <id>` | Delete task | `delete 1` |
| `help` | Show available commands | `help` |
| `exit`, `quit` | Exit application | `exit` |

## Important Notes

### ⚠️ Data is NOT Saved

**Tasks are stored in memory only**. When you exit the app, all tasks are permanently lost. This is by design for Phase I of the hackathon.

**Why?**: Phase I requirements specify in-memory storage only. Persistence (file or database) will be added in Phase II.

### Validation Rules

- **Title**: 1-200 characters (required)
- **Description**: 0-1000 characters (optional)
- **Task ID**: Positive integer, auto-assigned, never reused

### Performance

- Response time: < 100ms for all operations
- Capacity: Handles up to 1000 tasks efficiently
- Memory usage: ~1KB per task

## Project Structure

```
HackatonII/
├── src/
│   ├── __init__.py       # Package initialization
│   ├── models.py         # Task dataclass with validation
│   ├── task_manager.py   # Business logic (CRUD operations)
│   ├── cli.py            # CLI interface (command parsing, output)
│   └── main.py           # Application entry point
├── specs/                # Specification documents
│   └── master/
│       ├── spec.md       # Feature specification
│       ├── plan.md       # Implementation plan
│       ├── tasks.md      # Task breakdown
│       ├── data-model.md # Data model documentation
│       └── research.md   # Technology decisions
├── .gitignore
├── pyproject.toml        # UV project configuration
├── README.md             # This file
└── CLAUDE.md             # Claude Code development guide
```

## Development

### Architecture

**3-Layer Clean Architecture**:
- **Data Layer** (`models.py`): Task entity with validation
- **Business Logic** (`task_manager.py`): CRUD operations, in-memory storage
- **Interface Layer** (`cli.py`): Command parsing, output formatting

### Type Safety

All code uses Python type hints per constitution Principle II:
```python
def add_task(self, title: str, description: str = "") -> Task:
    ...
```

### Error Handling

All errors display user-friendly messages:
```python
try:
    task = manager.add_task(title, description)
except ValueError as e:
    print(f"Error: {e}")
```

## Troubleshooting

**Python 3.13 not found**:
- Install from [python.org](https://www.python.org/downloads/)

**UV not found**:
- Install using the commands in the Prerequisites section

**Module not found errors**:
- Ensure you're running from the `HackatonII` directory
- Use `uv run python src/main.py` instead of `python src/main.py`

**Virtual environment issues**:
- UV handles virtual environments automatically
- If needed, delete `.venv/` and run `uv venv` again

## Contributing

This is a hackathon project developed using spec-driven development (SDD) workflow:

1. **Specification** (`specs/master/spec.md`) - User stories and requirements
2. **Planning** (`specs/master/plan.md`) - Technical approach and architecture
3. **Tasks** (`specs/master/tasks.md`) - Task breakdown by user story
4. **Implementation** - Code generation with Claude Code

See `CLAUDE.md` for development instructions.

## License

This project is part of Hackathon II educational assignment.

## Acknowledgments

- Built with Claude Code using spec-driven development
- Follows constitution principles: Type Safety, Simplicity & Pragmatism, Observability
- Implements 5 Basic Level features per hackathon requirements

---

**Version**: 1.0.0 | **Phase**: Phase I (Console App) | **Date**: 2025-12-17
