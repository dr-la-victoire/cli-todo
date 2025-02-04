# CLI Todo App

A command-line tool to manage tasks and to-dos. This tool allows users to:

- View tasks
- Add a new task
- Delete a task
- Update task details (description, status, or due date)

## Features

- Stores tasks in a JSON file for persistence.
- Assigns unique IDs to tasks automatically.
- Allows users to mark tasks as pending or completed.
- Provides an intuitive command-line interface.

## Installation

1. Ensure you have Python installed on your system (I'm using Python 3.8.16).
2. Clone this repository or download the script.
3. Create an empty `task.json` file in the same directory to store tasks:
   ```json
   {}
   ```
4. Run the script from the terminal.

## Usage

Run the script using:

```sh
python main.py
```

(due to the peculiarities of my setup, I run by specifying python3.8)
You will be prompted with a menu to perform different actions.

## Task Status Options

- `pending`: The task is yet to be completed.
- `completed`: The task has been finished.

## Example Task Format (Stored in `task.json`)

```json
{
  "task1": {
    "description": "Complete Python project",
    "status": "pending",
    "due date": "10-02-2025"
  }
}
```

## Future Improvements

- Implement command-line arguments for task operations.
- Add a feature to list tasks by status (pending/completed).
- Improve error handling for file operations.

## License

This project is open-source and available for modification and distribution.
