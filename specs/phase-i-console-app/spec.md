# Feature Specification: Todo In-Memory Python Console App (Phase I)

**Feature Branch**: `001-phase-i-console-app`
**Created**: 2025-12-17
**Status**: Draft
**Phase**: Phase I (100 points, Due: Dec 7, 2025)
**Input**: Build a command-line todo application that stores tasks in memory using Claude Code and Spec-Kit Plus.

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Add New Todo Task (Priority: P1)

As a user, I want to add a new todo task with a title and optional description so that I can keep track of things I need to do.

**Why this priority**: This is the core functionality - without the ability to add tasks, the application has no purpose. This is the foundation for all other features.

**Independent Test**: Can be fully tested by running the console app, entering a task title and description, and verifying the task appears in the task list with a unique ID and "pending" status.

**Acceptance Scenarios**:

1. **Given** the console app is running, **When** I enter "Add task: Buy groceries", **Then** a new task is created with ID 1, title "Buy groceries", empty description, and status "pending"
2. **Given** the console app is running, **When** I enter "Add task: Call mom - description: Call to wish her happy birthday", **Then** a new task is created with title "Call mom", description "Call to wish her happy birthday", and status "pending"
3. **Given** I have already added 2 tasks, **When** I add a third task "Finish report", **Then** it is assigned ID 3 and stored in memory

---

### User Story 2 - View All Tasks (Priority: P1)

As a user, I want to view all my tasks in a list so that I can see what I need to do.

**Why this priority**: Without viewing tasks, users cannot see what they've added. This is essential for the MVP to be useful.

**Independent Test**: Can be fully tested by adding several tasks and then viewing the list, verifying all tasks appear with their IDs, titles, descriptions, and completion status.

**Acceptance Scenarios**:

1. **Given** I have no tasks, **When** I view the task list, **Then** I see "No tasks found"
2. **Given** I have 3 tasks added, **When** I view the task list, **Then** I see all 3 tasks with their ID, title, description, and status (✓ for complete, ○ for pending)
3. **Given** I have tasks with different statuses, **When** I view the list, **Then** completed tasks are visually distinguished from pending tasks

---

### User Story 3 - Mark Task as Complete (Priority: P2)

As a user, I want to mark a task as complete so that I can track my progress and know what I've finished.

**Why this priority**: This provides value by allowing users to track completion, but the app is still useful for capturing tasks even without this feature.

**Independent Test**: Can be fully tested by adding a task, marking it complete by ID, and verifying its status changes from pending to complete in the task list.

**Acceptance Scenarios**:

1. **Given** I have a pending task with ID 1, **When** I enter "Complete task 1", **Then** the task status changes to "complete" and is marked with ✓
2. **Given** I have a completed task with ID 2, **When** I enter "Uncomplete task 2", **Then** the task status changes back to "pending" and is marked with ○
3. **Given** I try to complete task ID 99 which doesn't exist, **When** I enter "Complete task 99", **Then** I see error message "Task ID 99 not found"

---

### User Story 4 - Update Task Details (Priority: P3)

As a user, I want to update a task's title or description so that I can correct mistakes or add more information.

**Why this priority**: Nice to have for improving task management, but core functionality works without it. Users can delete and re-add tasks as a workaround.

**Independent Test**: Can be fully tested by adding a task, updating its title or description, and verifying the changes are reflected when viewing the task list.

**Acceptance Scenarios**:

1. **Given** I have a task with ID 1 and title "Buy groceries", **When** I enter "Update task 1 title: Buy groceries and supplies", **Then** the task title is updated
2. **Given** I have a task with ID 2, **When** I enter "Update task 2 description: Need to finish by Friday", **Then** the task description is updated
3. **Given** I try to update task ID 99 which doesn't exist, **When** I enter "Update task 99", **Then** I see error message "Task ID 99 not found"

---

### User Story 5 - Delete Task (Priority: P3)

As a user, I want to delete a task so that I can remove tasks I no longer need to track.

**Why this priority**: Useful for cleanup, but not essential for core task management. Users can simply mark tasks as complete instead.

**Independent Test**: Can be fully tested by adding multiple tasks, deleting one by ID, and verifying it no longer appears in the task list.

**Acceptance Scenarios**:

1. **Given** I have a task with ID 1, **When** I enter "Delete task 1", **Then** the task is removed from the list
2. **Given** I have 3 tasks, **When** I delete task ID 2, **Then** only 2 tasks remain and task IDs 1 and 3 still exist
3. **Given** I try to delete task ID 99 which doesn't exist, **When** I enter "Delete task 99", **Then** I see error message "Task ID 99 not found"

---

### Edge Cases

- What happens when a user tries to add a task with an empty title?
  - System rejects the input and prompts "Title is required"
- What happens when a user enters an invalid command?
  - System displays "Invalid command. Type 'help' for available commands"
- What happens when a user tries to operate on a task ID that doesn't exist?
  - System displays "Task ID [X] not found"
- What happens when the user tries to add a task with a title longer than 200 characters?
  - System truncates to 200 characters and warns user
- What happens when the user tries to add a description longer than 1000 characters?
  - System truncates to 1000 characters and warns user
- What happens when the user exits the application?
  - All tasks are lost (in-memory only) with a warning message "Tasks are not saved. They will be lost when you exit."

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST allow users to add a new task with a title (required) and description (optional)
- **FR-002**: System MUST assign a unique sequential integer ID to each task starting from 1
- **FR-003**: System MUST store all tasks in memory (Python data structures - lists/dictionaries)
- **FR-004**: System MUST allow users to view all tasks with ID, title, description, and completion status
- **FR-005**: System MUST allow users to mark a task as complete or incomplete by task ID
- **FR-006**: System MUST allow users to update a task's title or description by task ID
- **FR-007**: System MUST allow users to delete a task by task ID
- **FR-008**: System MUST validate that task titles are 1-200 characters in length
- **FR-009**: System MUST validate that task descriptions are 0-1000 characters in length
- **FR-010**: System MUST provide clear error messages for invalid operations (task not found, invalid input)
- **FR-011**: System MUST provide a help command listing all available commands
- **FR-012**: System MUST run as a console/terminal application with text input/output
- **FR-013**: System MUST warn users that tasks are not persisted when exiting
- **FR-014**: System MUST implement clean code principles and proper Python project structure
- **FR-015**: System MUST follow the constitution principle of Simplicity & Pragmatism (no over-engineering)

### Technical Constraints

- **TC-001**: MUST use Python 3.13+
- **TC-002**: MUST use UV for package management
- **TC-003**: MUST be developed using Claude Code and Spec-Kit Plus
- **TC-004**: MUST NOT write code manually - refine specs until Claude Code generates correct output
- **TC-005**: MUST follow clean code principles per constitution
- **TC-006**: MUST use in-memory storage only (no database, no file persistence)
- **TC-007**: MUST implement type hints for type safety where applicable

### Key Entities *(include if feature involves data)*

- **Task**: Represents a todo item
  - **Attributes**:
    - `id` (int, unique, auto-increment)
    - `title` (str, 1-200 chars, required)
    - `description` (str, 0-1000 chars, optional)
    - `completed` (bool, default False)
    - `created_at` (datetime, auto-set)
    - `updated_at` (datetime, auto-updated)

- **TaskManager**: Manages the collection of tasks
  - **Responsibilities**:
    - Add, view, update, delete, and toggle task completion
    - Maintain task ID counter
    - Validate input
    - Provide help information

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Users can add a task in under 5 seconds with a single command
- **SC-002**: Users can view all tasks with clear visual distinction between complete and pending tasks
- **SC-003**: 100% of the 5 Basic Level features are implemented and functional (Add, Delete, Update, View, Mark Complete)
- **SC-004**: All error cases provide clear, actionable error messages
- **SC-005**: Application responds to all commands instantly (< 100ms response time)
- **SC-006**: Code follows clean code principles with proper separation of concerns
- **SC-007**: Application includes README.md with setup and usage instructions
- **SC-008**: Application includes CLAUDE.md with Claude Code development instructions
- **SC-009**: Specification, plan, and task files exist in /specs folder demonstrating spec-driven development process

### Non-Functional Requirements

- **NFR-001**: Code must be readable and maintainable with clear function/variable names
- **NFR-002**: Application must provide a good user experience with clear prompts and formatting
- **NFR-003**: Application must handle errors gracefully without crashing
- **NFR-004**: Code must include docstrings for main functions
- **NFR-005**: Project structure must be clean and logical (src/ folder for source code)

## Out of Scope

- Persistent storage (file or database) - Phase I is in-memory only
- User authentication - single user application
- Task due dates and reminders - Advanced Level features for later phases
- Task priorities and tags - Intermediate Level features for later phases
- Search and filter functionality - Intermediate Level features for later phases
- Task sorting - Intermediate Level features for later phases
- Recurring tasks - Advanced Level features for later phases
- Web interface - Phase II requirement
- AI chatbot interface - Phase III requirement
- Cloud deployment - Phase IV/V requirement

## Dependencies

- Python 3.13+ runtime environment
- UV package manager
- Claude Code for code generation
- Spec-Kit Plus for spec-driven workflow
- Text terminal/console for running the application

## Risks & Mitigation

| Risk | Impact | Mitigation |
|------|--------|------------|
| Claude Code generates incorrect implementation | High | Iteratively refine specifications with more detail and examples |
| User unfamiliar with command-line interface | Medium | Provide clear help documentation and intuitive command syntax |
| In-memory storage limitation causes confusion | Low | Display clear warning on exit about data loss |
| Validation edge cases not handled | Medium | Thoroughly specify all edge cases in spec before implementation |

## References

- Hackathon II PDF: Phase I Requirements (Pages 5-6)
- Constitution v1.1.0: Principle VII (Simplicity & Pragmatism)
- Constitution v1.1.0: Principle III (Test-Driven Development with hackathon pragmatism)
- Todo App Feature Progression: Basic Level (Page 2)
