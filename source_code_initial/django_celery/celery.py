# django_celery/celery.py                   <==== i've never seen this practice, i'll use in my codes from now on

from __future__ import absolute_import, unicode_literals
import os 
from celery import Celery


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_celery.settings")

app = Celery("django_celery")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()

# Configuro Celery para usar gevent
app.conf.update(
    worker_pool='gevent',
)