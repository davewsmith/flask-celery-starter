from celery import Celery
from flask import Flask

from config import Config


celery = Celery(__name__)

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # N.B., The Flask docs suggest celery.conf.update(), but that appears to
    # not work with celery 4.2.0
    celery.config_from_object(config_class)

    # Arrange for tasks to have access to the Flask app
    TaskBase = celery.Task
    class ContextTask(TaskBase):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs) 
    celery.Task = ContextTask

    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    return app
