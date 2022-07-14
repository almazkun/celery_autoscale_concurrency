import os

CELERY_APP_NAME = os.environ.get("CELERY_APP_NAME")
CELERY_BROKER_URL = os.environ.get("CELERY_BROKER_URL")
CELERY_BACKEND_URL = os.environ.get("CELERY_BACKEND_URL")

from celery import Celery


app = Celery(
    CELERY_APP_NAME,
    broker=CELERY_BROKER_URL,
    backend=CELERY_BACKEND_URL,
)
app.conf.update(
    accept_content=["application/json"],
    result_serializer="json",
    task_serializer="json",
)


@app.task
def one() -> str:
    from time import sleep

    sleep(10)
    return "Wake up"
