# TO-DO List Application

## Overview
The TO-DO List application is a simple task management tool designed to help users keep track of their tasks. Users can add new tasks, remove existing tasks, and save their tasks to a file for later retrieval.

## Features
- **Add Task:** Users can add new tasks to the list by entering task descriptions in the provided text field and clicking the "Add Task" button.
- **Remove Task:** Users can remove tasks from the list by selecting a task and clicking the "Remove Task" button.
- **Save Tasks:** Tasks are automatically saved to a file (`tasks.txt`) when added or removed, allowing users to persist their task list across sessions.
- **Load Tasks:** Upon launching the application, tasks are loaded from the `tasks.txt` file and displayed in the task list.

## Getting Started
1. **Installation**: No installation is required. Simply run the Python script (`todo.py`) to launch the application.

2. **Usage**: 
   - To add a task, enter the task description in the text field and click the "Add Task" button.
   - To remove a task, select the task from the list and click the "Remove Task" button.

3. **File Structure**:
   - `todo.py`: Main Python script containing the application code.
   - `customtkinter.py`: Custom tkinter module providing custom-styled widgets.
   - `tasks.txt`: Text file used to store tasks. Tasks are stored one per line.

## Dependencies
- Python 3.x
- tkinter (built-in)
