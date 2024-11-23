# Task CLI - Command-Line Task Tracker

## Overview

Task CLI is a simple, lightweight command-line interface (CLI) task management application built in Python. It allows users to add, update, delete, and track tasks with different statuses.

This is one of the exercises at roadmap.sh 
[Link to the project](https://roadmap.sh/projects/task-tracker)

## Features

- Add new tasks
- Update task descriptions
- Delete tasks
- Mark tasks as in-progress
- Mark tasks as done
- List tasks (all or filtered by status)
- Persistent storage using JSON

## Prerequisites

- Python 3.x
- No external dependencies required

## Installation

1. Clone this repository
2. Ensure you have Python 3.x installed
3. Navigate to the project directory

## Usage

### Commands

- Add a task:
  ```
  python task-cli.py add "Task description here"
  ```

- Update a task:
  ```
  python task-cli.py update <task_id> "New task description"
  ```

- Delete a task:
  ```
  python task-cli.py delete <task_id>
  ```

- Mark task as in-progress:
  ```
  python task-cli.py mark-in-progress <task_id>
  ```

- Mark task as done:
  ```
  python task-cli.py mark-done <task_id>
  ```

- List all tasks:
  ```
  python task-cli.py list
  ```

- List tasks by status (todo/in-progress/done):
  ```
  python task-cli.py list <status>
  ```

## Task Statuses

- `todo`: Default status for new tasks
- `in-progress`: Tasks currently being worked on
- `done`: Completed tasks

## Data Storage

Tasks are stored in `tasks.json` in the same directory as the script. The file is automatically created and updated when you manage tasks.
