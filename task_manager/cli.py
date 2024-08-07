from models import Task, Project, User
from database import session
from datetime import datetime, date

def create_user():
    """Create a new user"""
    name = input("Enter user name: ")
    user = User(name=name)
    session.add(user)
    session.commit()
    print(f"User {name} created successfully.")

def create_project():
    """Create a new project"""
    name = input("Enter project name: ")
    user_id = int(input("Enter user ID: "))
    project = Project(name=name, user_id=user_id)
    session.add(project)
    session.commit()
    print(f"Project {name} created successfully.")

def create_task():
    """Create a new task"""
    name = input("Enter task name: ")
    description = input("Enter task description: ")
    user_id = int(input("Enter user ID: "))
    project_id = int(input("Enter project ID: "))
    due_date_str = input("Enter due date (YYYY-MM-DD) (optional): ")
    due_date = datetime.strptime(due_date_str, '%Y-%m-%d').date() if due_date_str else None
    priority = int(input("Enter priority (1-5) (optional): ") or 0)
    task = Task(name=name, description=description, user_id=user_id, project_id=project_id, due_date=due_date, priority=priority)
    session.add(task)
    session.commit()
    print(f"Task {name} created successfully.")

def list_tasks():
    """List all tasks"""
    tasks = session.query(Task).order_by(Task.due_date.asc(), Task.priority.desc()).all()
    if tasks:
        for task in tasks:
            print(f'{task.id}: {task.name} - {task.description} - Due: {task.due_date} - Priority: {task.priority}')
    else:
        print("No tasks found.")

def list_projects():
    """List all projects"""
    projects = session.query(Project).all()
    if projects:
        for project in projects:
            print(f'{project.id}: {project.name} - User ID: {project.user_id}')
    else:
        print("No projects found.")

def list_upcoming_tasks():
    """List upcoming tasks"""
    today = date.today()
    tasks = session.query(Task).filter(Task.due_date >= today).order_by(Task.due_date.asc()).all()
    if tasks:
        for task in tasks:
            print(f'{task.id}: {task.name} - {task.description} - Due: {task.due_date} - Priority: {task.priority}')
    else:
        print("No upcoming tasks found.")

def main_menu():
    """Main menu to navigate the CLI"""
    while True:
        print("\nMain Menu:")
        print("1. Create User")
        print("2. Create Project")
        print("3. Create Task")
        print("4. List Tasks")
        print("5. List Projects")
        print("6. List Upcoming Tasks")
        print("7. Exit")
        choice = input("Please choose an option: ")

        if choice == '1':
            create_user()
        elif choice == '2':
            create_project()
        elif choice == '3':
            create_task()
        elif choice == '4':
            list_tasks()
        elif choice == '5':
            list_projects()
        elif choice == '6':
            list_upcoming_tasks()
        elif choice == '7':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    print("Welcome to the Task Manager CLI!")
    main_menu()









