import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NewsPaper.settings')

app = Celery('NewsPaper')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'action_every_monday_8am': {
        'task': 'news.tasks.send_weekly_mail',
        'schedule': crontab(minute='0', hour='8', day_of_week='monday'),
    },
}

app.autodiscover_tasks()
