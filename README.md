# Phase-3-Final

# Task Manager CLI

## Overview

Task Manager CLI is a command-line application designed to help users manage tasks, projects, and users. It uses SQLAlchemy for ORM and a SQLite database to store data.

## Features

- **Create User**: Add a new user to the system.
- **Create Project**: Add a new project associated with a user.
- **Create Task**: Add a new task associated with a project and a user.
- **List Tasks**: Display all tasks in the system.
- **Exit**: Exit the application.

## Requirements

- Python 3.8 or higher
- Pipenv (for managing virtual environments and dependencies)

## Installation

1. **Clone the Repository**
   ```sh
   git clone https://github.com/YOUR_USERNAME/task-manager-cli.git
   cd task-manager-cli
   ```

## Set Up Virtual Environment

pipenv install
pipenv shell

## Usage

Run the Application
Copy code
python3 task_manager/cli.py
Follow the Menu Prompts
The main menu will display options for creating users, projects, tasks, listing tasks, or exiting the application.
Enter the number corresponding to your choice and follow the prompts to enter the required information.

## File Structure

Copy code
task_manager/

- \*\*├── models.py # SQLAlchemy models for User, Project, and Task
- \*\* cli.py # Main CLI application code
- \*\* database.py # Database setup and session creation
- \*\* **init**.py # Package initializer
- \*\* Pipfile # Pipenv configuration file
- \*\* Pipfile.lock # Pipenv lock file
- \*\* README.md # Project documentation

## Example

Starting the Application
sh
Copy code
$ python3 task_manager/cli.py
Welcome to the Task Manager CLI!

Main Menu:

1. Create User
2. Create Project
3. Create Task
4. List Tasks
5. Exit

## Contributing

- \*\*Fork the repository.
- \*\*Create a new branch (git checkout -b feature-branch).
- \*\*Make your changes.
- \*\*Commit your changes (git commit -am 'Add new feature').
- \*\*Push to the branch (git push origin feature-branch).
- \*\*Create a new Pull Request.
