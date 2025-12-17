# Phase 0 Research: Technology Decisions for Todo Console App

**Feature Branch**: `001-phase-i-console-app`
**Date**: 2025-12-17
**Phase**: Phase 0 (Research & Technology Decisions)

## Research Questions & Findings

### 1. Python 3.13+ Best Practices for Console Apps

**Question**: What are the recommended patterns for building console applications in Python 3.13+?

**Findings**:

1. **Command Parsing Approaches**:
   - **Simple input loop** (SELECTED): Best for straightforward command sets, minimal overhead
   - **argparse**: Better for complex CLI tools with subcommands and flags
   - **Click/Typer**: Third-party frameworks - unnecessary for simple apps (violates YAGNI)

2. **Clean Architecture Patterns**:
   - Separate concerns into layers: Data (models) → Logic (manager) → Interface (CLI)
   - Use dataclasses for entities (Python 3.7+)
   - Keep business logic independent of UI
   - Single Responsibility Principle: one class, one job

3. **Error Handling**:
   - Use try-except blocks at entry points
   - Return user-friendly messages, not stack traces
   - Validate input early (fail fast principle)
   - Use specific exception types for different error cases

**Decision**: Simple input loop with clean three-layer architecture (models, manager, CLI).

---

### 2. Data Modeling with Python Dataclasses

**Question**: How should we model the Task entity using Python dataclasses?

**Findings**:

1. **Dataclass Benefits**:
   - Automatic `__init__`, `__repr__`, `__eq__` generation
   - Type hints integrated into class definition
   - `__post_init__` for validation logic
   - Immutable option with `frozen=True` (not needed here)

2. **Type Hints**:
   - Use built-in types: `int`, `str`, `bool`
   - Use `datetime` from standard library for timestamps
   - Type hints enable IDE autocomplete and static analysis

3. **Validation Strategies**:
   - `__post_init__` method runs after `__init__`
   - Raise `ValueError` for validation failures
   - Keep validation logic in the entity itself (domain-driven design)

4. **Field Options**:
   - `field(default=...)` for default values
   - `field(default_factory=...)` for mutable defaults (like lists)
   - `field(init=False)` for computed fields

**Example Pattern**:

```python
from dataclasses import dataclass
from datetime import datetime

@dataclass
class Task:
    id: int
    title: str
    description: str
    completed: bool
    created_at: datetime
    updated_at: datetime

    def __post_init__(self):
        if not self.title or len(self.title) < 1:
            raise ValueError("Title is required")
        if len(self.title) > 200:
            raise ValueError("Title must be 200 characters or less")
        if len(self.description) > 1000:
            raise ValueError("Description must be 1000 characters or less")
```

**Decision**: Use dataclasses with type hints and validation in `__post_init__`.

---

### 3. In-Memory Storage Patterns

**Question**: What is the best data structure for storing tasks in memory?

**Findings**:

1. **Storage Options**:
   - **Dict by ID** (SELECTED): O(1) lookup, natural fit for CRUD operations
   - **List only**: O(n) lookup by ID, simple but inefficient for large datasets
   - **List + Dict index**: Over-engineering for Phase I requirements

2. **ID Generation Strategies**:
   - **Incrementing counter** (SELECTED): Simple, predictable, sufficient for single-user
   - **UUID**: Unnecessary complexity for in-memory single-user app
   - **Timestamp-based**: Collision risk, not sequential

3. **Search/Filter Performance**:
   - Dict lookup by ID: O(1) - instant
   - Iterate all tasks: O(n) - acceptable for up to 1000 tasks
   - No complex indexing needed for Phase I requirements

**Storage Structure**:

```python
class TaskManager:
    def __init__(self):
        self.tasks: dict[int, Task] = {}  # ID → Task mapping
        self.next_id: int = 1              # Auto-increment counter
```

**Decision**: Dict storage with auto-incrementing integer IDs.

---

### 4. User Experience for CLI Apps

**Question**: How should we design the command syntax and output formatting?

**Findings**:

1. **Command Syntax Patterns**:
   - **Natural language** (SELECTED): `add Buy groceries`, `complete 1`, `delete 2`
   - **Flag-based**: `--add "Buy groceries"` - more complex, less intuitive
   - **Menu-driven**: Numbered menus - more steps, slower interaction

2. **Output Formatting**:
   - Use Unicode box-drawing characters for tables (✓, ○, │, ─)
   - Clear column headers
   - Visual distinction between completed (✓) and pending (○) tasks
   - Consistent spacing and alignment

3. **Help Documentation**:
   - Built-in `help` command listing all available commands
   - Show examples for each command
   - Keep it concise but comprehensive

4. **User Feedback**:
   - Confirm actions: "Task 1 added successfully"
   - Show impact: "Task 2 marked as complete"
   - Clear error messages: "Task ID 99 not found"

**Example Output**:

```
ID │ Status │ Title                    │ Description
───┼────────┼─────────────────────────┼────────────────────
1  │ ○      │ Buy groceries            │ milk, eggs, bread
2  │ ✓      │ Call mom                 │ Birthday wishes
3  │ ○      │ Finish report            │ Q4 summary
```

**Decision**: Natural language commands with formatted table output.

---

## Technology Decisions Summary

| Decision | Choice | Rationale | Alternatives Considered |
|----------|--------|-----------|------------------------|
| **Language** | Python 3.13+ | Hackathon requirement | N/A (specified requirement) |
| **Package Manager** | UV | Hackathon requirement, fast Python package manager | pip, poetry (UV is required) |
| **Dependencies** | Standard library only | Simplicity principle, no external dependencies needed | Click/Typer for CLI (unnecessary for simple input loop) |
| **Entity Modeling** | Dataclasses with type hints | Type safety, clean syntax, Python 3.7+ standard | Named tuples (less flexible), plain dicts (no type safety) |
| **Storage Structure** | Dict[int, Task] | O(1) lookup by ID, natural fit for CRUD | List only (O(n) lookup, less efficient) |
| **ID Strategy** | Auto-incrementing int | Simple, predictable, sufficient for single-user | UUID (unnecessary complexity) |
| **CLI Pattern** | Simple input loop | YAGNI principle, sufficient for requirements | argparse/Click (over-engineering) |
| **Command Syntax** | Natural language | Intuitive, user-friendly | Flag-based (more complex, less intuitive) |
| **Output Format** | Unicode table with box-drawing chars | Clear visual distinction, professional appearance | Plain text (less readable) |

---

## Architecture Pattern

**Selected Pattern**: Three-Layer Clean Architecture

```
┌─────────────────────────────────────────┐
│          main.py (Entry Point)          │
│  - Initializes TaskManager              │
│  - Initializes CLI                      │
│  - Starts main loop                     │
└──────────────────┬──────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────┐
│          cli.py (User Interface)        │
│  - Reads user input                     │
│  - Parses commands                      │
│  - Formats output                       │
│  - Displays errors/help                 │
└──────────────────┬──────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────┐
│    task_manager.py (Business Logic)     │
│  - add_task(title, description)         │
│  - get_all_tasks()                      │
│  - get_task(id)                         │
│  - update_task(id, title, description)  │
│  - complete_task(id, status)            │
│  - delete_task(id)                      │
│  - validate_input()                     │
└──────────────────┬──────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────┐
│        models.py (Data Layer)           │
│  - Task dataclass                       │
│  - Field validation                     │
└─────────────────────────────────────────┘
```

**Why this pattern?**:
- **Separation of Concerns**: Each layer has a single responsibility
- **Testability**: Each layer can be tested independently
- **Maintainability**: Changes to UI don't affect business logic
- **Simplicity**: No unnecessary abstractions or over-engineering

---

## Performance Considerations

**Requirement**: < 100ms response time, handle up to 1000 tasks

**Analysis**:

1. **Dict Lookup**: O(1) - instant, no performance concern
2. **List All Tasks**: O(n) - 1000 iterations minimal overhead in Python
3. **Update/Delete**: O(1) dict access + O(1) update/delete
4. **Validation**: O(1) string length checks

**Conclusion**: All operations well within < 100ms requirement. No optimization needed for Phase I.

---

## Security & Validation

**Input Validation**:
- Title: 1-200 characters (required)
- Description: 0-1000 characters (optional)
- Task ID: Must be positive integer
- Command parsing: Validate format before execution

**Security Considerations**:
- No file system access (in-memory only)
- No network access
- No code execution from user input
- No SQL injection risk (no database)

**Conclusion**: Minimal security concerns for Phase I console app.

---

## Constitution Compliance Check

| Principle | Compliance | Notes |
|-----------|------------|-------|
| I. Full-Stack Architecture | N/A for Phase I | Console app only; applies to Phase II+ |
| II. Type Safety First | ✅ PASS | Type hints for all functions, dataclasses with typed fields |
| III. Test-Driven Development | ✅ PASS (Pragmatic) | Tests recommended but not blocking per hackathon exception |
| IV. Integration Testing | N/A for Phase I | No external integrations in console app |
| V. Observability | ✅ PASS (Simplified) | Clear error messages, user feedback for all operations |
| VI. Versioning & Breaking Changes | ✅ PASS | Version 1.0.0 for initial release |
| VII. Simplicity & Pragmatism | ✅ PASS | No over-engineering, standard library only, YAGNI applied |

---

## Open Questions & Risks

**Open Questions**: None remaining after research.

**Risks**:

1. **Risk**: Command parsing ambiguity
   - **Mitigation**: Clear command syntax documentation, helpful error messages

2. **Risk**: Users forget data is not saved
   - **Mitigation**: Display warning on exit, mention in help command

3. **Risk**: ID collision after deletion
   - **Mitigation**: Use incrementing counter, don't reuse IDs

4. **Risk**: Input validation edge cases
   - **Mitigation**: Comprehensive validation in Task model and TaskManager

---

## Next Steps

✅ Phase 0 Research Complete

**Phase 1 Artifacts**:
- Create `data-model.md` - Detailed Task entity specification
- Create `quickstart.md` - Installation and usage instructions

**Phase 2**:
- Run `/sp.tasks` to generate actionable task breakdown

**Phase 3**:
- Run `/sp.implement` to execute tasks with Claude Code

---

**References**:
- Python Dataclasses: https://docs.python.org/3/library/dataclasses.html
- PEP 8 Style Guide: https://peps.python.org/pep-0008/
- Python Type Hints: https://docs.python.org/3/library/typing.html
- Clean Architecture Principles: Robert C. Martin, "Clean Architecture"
