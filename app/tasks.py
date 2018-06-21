import celery
import logging


logger = logging.getLogger(__name__)

@celery.task(name="add")
def add(a, b):
    logger.info("in the task")
    return a + b
