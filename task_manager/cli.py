import click
from models import Task, Project, User, session

@click.group()
def cli():
    pass

@cli.command()
def create_user(name):
    user = User(name=name)
    session.add(user)
    session.commit()

@cli.command()
def create_project(name, user_id):
    project = Project(name=name, user_id=user_id)
    session.add(project)
    session.commit()

@cli.command()
def create_task(name, description, user_id, project_id):
    task = Task(name=name, description=description, user_id=user_id, project_id=project_id)
    session.add(task)
    session.commit()

@cli.command()
def list_tasks():
    tasks = session.query(Task).all()
    for task in tasks:
        click.echo(f'{task.id}: {task.name}')

if __name__ == '__main__':
    cli()
