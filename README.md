# Task Manager CLI

## About

Task Manager CLI is a command-line application designed to help users efficiently manage their tasks, projects, and users. This application was created as part of a software engineering bootcamp project to demonstrate proficiency in Python, SQLAlchemy ORM, and command-line interface development.

The primary goal of Task Manager CLI is to provide a simple yet powerful tool for organizing tasks and projects in a way that is easy to use from the terminal. With features such as creating users, projects, and tasks, as well as listing tasks, this application aims to streamline task management for developers and other tech-savvy users who prefer using the command line.

By integrating Alembic for database migrations, Task Manager CLI ensures that schema changes can be managed smoothly, making it easier to maintain and scale the application as it evolves.

## Features

- **Create User**: Add a new user to the system.
- **Create Project**: Add a new project associated with a user.
- **Create Task**: Add a new task associated with a project and a user, including due dates and priority levels.
- **List Tasks**: Display all tasks in the system, sorted by due date and priority.
- **List Projects**: Display all projects in the system.
- **List Upcoming Tasks**: Display tasks that are due today or in the future.
- **Exit**: Exit the application.

## Requirements

- Python 3.8 or higher
- Pipenv (for managing virtual environments and dependencies)

## Installation

**Clone the Repository**

git clone https://github.com/YOUR_USERNAME/task-manager-cli.git
cd task-manager-cli

**Set Up Virtual Environment**

- \*\*pipenv install
- \*\*pipenv shell
- \*\*pipenv install sqlalchemy alembic
- \*\*Initialize Alembic
- \*\*alembic init alembic
- \*\*Update alembic.ini with your database connection string:

> Update alembic/env.py to Include Your Models
> Edit alembic/env.py to import your models and target the metadata:
> from models import Base
> target_metadata = Base.metadata
> Create Initial Migration
> alembic revision --autogenerate -m "Add due_date and priority to Task"
> Apply the Migration
> alembic upgrade head

## File Structure

graphql
Copy code
task_manager/
├── alembic/ # Alembic migrations directory
│ ├── versions/
│ └── env.py
├── models.py # SQLAlchemy models for User, Project, and Task
├── cli.py # Main CLI application code
├── database.py # Database setup and session creation
├── **init**.py # Package initializer
├── alembic.ini # Alembic configuration file
├── Pipfile # Pipenv configuration file
├── Pipfile.lock # Pipenv lock file
├── README.md # Project documentation

## Usage

Run the Application
python3 task_manager/cli.py
Follow the Menu Prompts
The main menu will display options for creating users, projects, tasks, listing tasks, listing projects, listing upcoming tasks, or exiting the application.
Enter the number corresponding to your choice and follow the prompts to enter the required information.

## Contributing

Fork the repository.
Create a new branch (git checkout -b feature-branch).
Make your changes.
Commit your changes (git commit -am 'Add new feature').
Push to the branch (git push origin feature-branch).
Create a new Pull Request.
