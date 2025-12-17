"""Command-line interface for the Todo application.

This module handles user input parsing, command execution, and output formatting.
"""

from typing import Optional

from task_manager import TaskManager


class CLI:
    """Command-line interface for task management.

    Attributes:
        manager: TaskManager instance for business logic
    """

    def __init__(self, manager: TaskManager) -> None:
        """Initialize CLI with a TaskManager instance.

        Args:
            manager: TaskManager instance to use for task operations
        """
        self.manager = manager

    def parse_add_command(self, command: str) -> tuple[str, str]:
        """Parse 'add' command to extract title and description.

        Command formats:
        - "add <title>"
        - "add <title> - <description>"

        Args:
            command: Full command string starting with "add"

        Returns:
            Tuple of (title, description)
        """
        # Remove "add" prefix and strip whitespace
        content = command[3:].strip()

        # Check for description separator " - "
        if " - " in content:
            parts = content.split(" - ", 1)
            title = parts[0].strip()
            description = parts[1].strip()
        else:
            title = content
            description = ""

        return title, description

    def handle_add_command(self, command: str) -> None:
        """Handle 'add' command - create new task.

        Args:
            command: Full command string starting with "add"
        """
        try:
            title, description = self.parse_add_command(command)

            if not title:
                print("Error: Title is required")
                return

            task = self.manager.add_task(title, description)
            print(f"Task {task.id} added successfully")

        except ValueError as e:
            print(f"Error: {e}")

    def format_task_table(self, tasks: list) -> str:
        """Format tasks as a table with columns for ID, Status, Title, Description.

        Args:
            tasks: List of Task objects to display

        Returns:
            Formatted table string
        """
        if not tasks:
            return "No tasks found"

        # Build table
        lines = []
        lines.append("ID | Status | Title                    | Description")
        lines.append("---|--------|--------------------------|--------------------")

        for task in tasks:
            status = "[X]" if task.completed else "[ ]"
            # Truncate title to 24 chars, description to 20 chars for table formatting
            title_display = task.title[:24] if len(task.title) <= 24 else task.title[:21] + "..."
            desc_display = task.description[:20] if len(task.description) <= 20 else task.description[:17] + "..."

            lines.append(f"{task.id:<2} | {status}  | {title_display:<24} | {desc_display}")

        # Add summary
        completed_count = sum(1 for t in tasks if t.completed)
        pending_count = len(tasks) - completed_count
        lines.append("")
        lines.append(f"{len(tasks)} tasks total ({completed_count} completed, {pending_count} pending)")

        return "\n".join(lines)

    def handle_list_command(self) -> None:
        """Handle 'list'/'view'/'show' command - display all tasks."""
        tasks = self.manager.get_all_tasks()
        output = self.format_task_table(tasks)
        print(output)

    def handle_complete_command(self, command: str) -> None:
        """Handle 'complete'/'done' command - mark task as complete.

        Args:
            command: Full command string like "complete 1" or "done 1"
        """
        try:
            # Extract task ID
            parts = command.split()
            if len(parts) < 2:
                print("Error: Please specify a task ID (e.g., 'complete 1')")
                return

            task_id_str = parts[1]
            if not task_id_str.isdigit():
                print("Error: Invalid task ID. Please enter a number.")
                return

            task_id = int(task_id_str)
            task = self.manager.complete_task(task_id, completed=True)
            print(f"Task {task_id} marked as complete")

        except ValueError as e:
            print(f"Error: {e}")

    def handle_uncomplete_command(self, command: str) -> None:
        """Handle 'uncomplete' command - mark task as incomplete.

        Args:
            command: Full command string like "uncomplete 1"
        """
        try:
            # Extract task ID
            parts = command.split()
            if len(parts) < 2:
                print("Error: Please specify a task ID (e.g., 'uncomplete 1')")
                return

            task_id_str = parts[1]
            if not task_id_str.isdigit():
                print("Error: Invalid task ID. Please enter a number.")
                return

            task_id = int(task_id_str)
            task = self.manager.complete_task(task_id, completed=False)
            print(f"Task {task_id} marked as incomplete")

        except ValueError as e:
            print(f"Error: {e}")

    def handle_update_command(self, command: str) -> None:
        """Handle 'update' command - update task title or description.

        Command formats:
        - "update <id> title <new_title>"
        - "update <id> description <new_description>"

        Args:
            command: Full command string starting with "update"
        """
        try:
            # Parse: update <id> <field> <value>
            parts = command.split(None, 3)  # Split into max 4 parts
            if len(parts) < 4:
                print("Error: Invalid update command. Use 'update <id> title <text>' or 'update <id> description <text>'")
                return

            task_id_str = parts[1]
            if not task_id_str.isdigit():
                print("Error: Invalid task ID. Please enter a number.")
                return

            task_id = int(task_id_str)
            field = parts[2].lower()
            value = parts[3]

            if field == "title":
                self.manager.update_task(task_id, title=value)
                print(f"Task {task_id} updated successfully")
            elif field == "description":
                self.manager.update_task(task_id, description=value)
                print(f"Task {task_id} updated successfully")
            else:
                print(f"Error: Unknown field '{field}'. Use 'title' or 'description'")

        except ValueError as e:
            print(f"Error: {e}")

    def handle_delete_command(self, command: str) -> None:
        """Handle 'delete'/'remove' command - delete a task.

        Args:
            command: Full command string like "delete 1" or "remove 1"
        """
        try:
            # Extract task ID
            parts = command.split()
            if len(parts) < 2:
                print("Error: Please specify a task ID (e.g., 'delete 1')")
                return

            task_id_str = parts[1]
            if not task_id_str.isdigit():
                print("Error: Invalid task ID. Please enter a number.")
                return

            task_id = int(task_id_str)
            self.manager.delete_task(task_id)
            print(f"Task {task_id} deleted successfully")

        except ValueError as e:
            print(f"Error: {e}")

    def handle_help_command(self) -> None:
        """Handle 'help' command - show available commands."""
        help_text = """
================================================================
                    Available Commands
================================================================

Task Management:
  add <title>                      Add new task with title only
  add <title> - <description>      Add new task with description
  list, view, show                 Display all tasks
  complete <id>, done <id>         Mark task as complete
  uncomplete <id>                  Mark task as incomplete
  update <id> title <text>         Update task title
  update <id> description <text>   Update task description
  delete <id>, remove <id>         Delete a task

System:
  help                             Show this help message
  exit, quit                       Exit application

Examples:
  > add Buy groceries
  > add Buy groceries - milk, eggs, bread
  > list
  > complete 1
  > update 1 title Buy groceries and supplies
  > delete 2
"""
        print(help_text)

    def handle_exit_command(self) -> bool:
        """Handle 'exit'/'quit' command - confirm and exit.

        Returns:
            True if user confirms exit, False to continue
        """
        print("\nWARNING: Tasks are not saved. They will be lost when you exit.")
        response = input("Are you sure you want to exit? (yes/no): ").strip().lower()

        if response in ["yes", "y"]:
            print("\nGoodbye!")
            return True

        print("Continuing...")
        return False

    def process_command(self, command: str) -> bool:
        """Process a user command.

        Args:
            command: User input command string

        Returns:
            True to continue running, False to exit
        """
        command = command.strip()
        command_lower = command.lower()

        if not command:
            return True

        # Route commands
        if command_lower.startswith("add "):
            self.handle_add_command(command)
        elif command_lower in ["list", "view", "show"]:
            self.handle_list_command()
        elif command_lower.startswith("complete ") or command_lower.startswith("done "):
            self.handle_complete_command(command)
        elif command_lower.startswith("uncomplete "):
            self.handle_uncomplete_command(command)
        elif command_lower.startswith("update "):
            self.handle_update_command(command)
        elif command_lower.startswith("delete ") or command_lower.startswith("remove "):
            self.handle_delete_command(command)
        elif command_lower == "help":
            self.handle_help_command()
        elif command_lower in ["exit", "quit"]:
            return not self.handle_exit_command()  # Return False if user confirms exit
        else:
            print("Invalid command. Type 'help' for available commands")

        return True
