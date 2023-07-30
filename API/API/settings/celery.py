from __future__ import absolute_import, unicode_literals

import os

from celery import Celery
from gradio_client import Client

from API.settings.dev import ML_URL

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'API.settings.dev')

ml_client = Client(ML_URL, verbose=False)

app = Celery('API')

app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()