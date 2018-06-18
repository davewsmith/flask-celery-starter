from flask import (
    render_template,
)

from app.main import bp

@bp.route('/')
def index():
    bindings = dict()
    return render_template('index.html', **bindings)
