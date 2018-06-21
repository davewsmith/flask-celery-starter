from app import (
    create_app,
    celery,
)


app = create_app()

@app.shell_context_processor
def make_shell_context():
    # Exports for `flask shell`
    return {
        # 'app' is exported automagically
        'celery': celery,
    }

