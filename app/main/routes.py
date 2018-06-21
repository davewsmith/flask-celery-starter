import logging
import random

from flask import (
    current_app,
    render_template,
)

from app.main import bp
from app.tasks import add


logger = logging.getLogger(__name__)

@bp.route('/')
def index():
    a = random.randint(1, 100)
    b = random.randint(1, 100)

    task = add.delay(a, b)
    current_app.logger.info("task.id = {}".format(task.id))
    answer = task.get()

    bindings = dict(
        a=a,
        b=b,
        task_id=task.id,
        answer=answer,
    )
    return render_template('index.html', **bindings)
