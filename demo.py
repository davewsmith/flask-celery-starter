import click

from app import (
    create_app,
    celery,
)
from app import tasks


app = create_app()

@app.shell_context_processor
def make_shell_context():
    # Exports for `flask shell`
    return {
        # 'app' is exported automagically
        'celery': celery,
    }

@app.cli.command()
@click.argument('a')
@click.argument('b')
def add(a, b):
    task = tasks.add.delay(int(a), int(b))
    result = task.get()
    print("task {} said {}".format(task.id, result))
