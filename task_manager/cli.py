from models import Task, Project, User
from database import session

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
    user_id = input("Enter user ID: ")
    project = Project(name=name, user_id=user_id)
    session.add(project)
    session.commit()
    print(f"Project {name} created successfully.")

def create_task():
    """Create a new task"""
    name = input("Enter task name: ")
    description = input("Enter task description: ")
    user_id = input("Enter user ID: ")
    project_id = input("Enter project ID: ")
    task = Task(name=name, description=description, user_id=user_id, project_id=project_id)
    session.add(task)
    session.commit()
    print(f"Task {name} created successfully.")

def list_tasks():
    """List all tasks"""
    tasks = session.query(Task).all()
    if tasks:
        for task in tasks:
            print(f'{task.id}: {task.name} - {task.description}')
    else:
        print("No tasks found.")

def main_menu():
    """Main menu to navigate the CLI"""
    while True:
        print("\nMain Menu:")
        print("1. Create User")
        print("2. Create Project")
        print("3. Create Task")
        print("4. List Tasks")
        print("5. Exit")
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
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    print("Welcome to the Task Manager CLI!")
    main_menu()






