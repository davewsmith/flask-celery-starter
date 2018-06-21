from app import (
    create_app,
    celery,
)

# Creating the app has the side-effect of configured celery
app = create_app()

from app.tasks import *  # noqa

