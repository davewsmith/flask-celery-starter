import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'top sekret'

    # Celery Configuration
    broker_url = 'redis://localhost:6379'
    result_backend = 'redis://localhost:6379'
    # This keeps celery from screwing up logging on the Flask side
    celery_hijack_root_logger = False

