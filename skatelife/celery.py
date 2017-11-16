from __future__ import absolute_import

import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'skatelife.settings.dev')

app = Celery('skatelife')

app.config_from_object('django.conf:settings')

app.autodiscover_tasks()
app.conf.result_backend = 'redis://localhost/0'
