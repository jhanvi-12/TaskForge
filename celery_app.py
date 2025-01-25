from __future__ import absolute_import, unicode_literals

import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'task_and_product_management.settings')

# Intialize the celery configuration and tassk.
app = Celery('task_and_product_management')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
