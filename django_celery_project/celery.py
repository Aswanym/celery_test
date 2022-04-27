import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab
# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_celery_project.settings')

app = Celery('django_celery_project')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object(settings, namespace='CELERY')

#celery beat settings
app.conf.beat_schedule ={

    'test_hello_func_everyday_at':{
        'task':'mainapp.tasks.test_hello_func',
        'schedule':crontab(hour="*/3")
    },
    'test_another_func_everyday':{
        'task':'mainapp.tasks.test_another_func',
        'schedule':crontab(minute="*/5")

    }
}

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')