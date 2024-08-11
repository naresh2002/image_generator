from __future__ import absolute_import, unicode_literals
from celery import Celery
import os

# Set default Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'image_generator.settings')

# Create a Celery instance
app = Celery('image_generator')

# Load settings from Django settings, the `CELERY` namespace means all celery-related settings keys should start with `CELERY_`
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs
app.autodiscover_tasks()
