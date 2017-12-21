from celery import Celery
from server.config.settings import INSTALLED_APPS

celery = Celery(
    'celery_app',
    broker='amqp://guest:guest@localhost:5672/',
)

celery.autodiscover_tasks(lambda: INSTALLED_APPS)
