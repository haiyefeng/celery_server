# import requests
# import logging

from celery_tasks.celery import app


# logger = logging.getLogger("celery")


@app.task
def add(x, y):
    return x + y


# celery -A celery_tasks.tasks worker -l info -Q add
