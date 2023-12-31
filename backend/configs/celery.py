import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "configs.settings")

app = Celery("settings")
app.config_from_object("django.conf.settings", namespace="CELERY")

app.autodiscover_tasks()

app.conf.beat_schedule = {
    "fetch_currencies_every_24_hours": {
        "task": "core.services.currency_service.execute_currencies",
        "schedule": crontab(minute=0, hour=23),
    }
}
