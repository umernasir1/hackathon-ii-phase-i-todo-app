"""Main entry point for the Todo Console Application.

This module initializes the TaskManager and CLI, displays the welcome banner,
and runs the main command loop.
"""

import sys
from cli import CLI
from task_manager import TaskManager


def display_banner() -> None:
    """Display welcome banner on app startup."""
    banner = """
================================================================
        Todo Console App - Phase I
  Type 'help' for available commands
  Type 'exit' to quit
================================================================
"""
    print(banner)


def main() -> None:
    """Main application entry point."""
    try:
        # Initialize components
        manager = TaskManager()
        cli = CLI(manager)

        # Display welcome banner
        display_banner()

        # Main command loop
        running = True
        while running:
            try:
                command = input("\n> ").strip()
                running = cli.process_command(command)
            except KeyboardInterrupt:
                # Handle Ctrl+C gracefully
                print("\n\nInterrupted by user. Type 'exit' to quit safely.")
                continue
            except EOFError:
                # Handle Ctrl+D gracefully
                print("\n\nGoodbye!")
                break

    except Exception as e:
        print(f"\nFatal error: {e}")
        print("The application encountered an unexpected error and must exit.")


if __name__ == "__main__":
    main()
