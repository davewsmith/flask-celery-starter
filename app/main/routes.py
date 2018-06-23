import logging
import random
import time

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

    started = time.time()
    task = add.delay(a, b)
    current_app.logger.info("task.id = {}".format(task.id))
    answer = task.get()
    elapsed = time.time() - started

    bindings = dict(
        a=a,
        b=b,
        task_id=task.id,
        elapsed=elapsed,
        answer=answer,
    )
    return render_template('index.html', **bindings)
