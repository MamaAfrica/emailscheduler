from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
# os.environ.setdefault('FORKED_BY_MULTIPROCESSING', '1')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'emailscheduler.settings')
app = Celery('emailscheduler', backend='redis://:pb5f0320b5e776373194182c60862bc79709c2afe6906420bfcfc3000999ddf9e@ec2-23-21-106-145.compute-1.amazonaws.com:14339', broker='redis://:pb5f0320b5e776373194182c60862bc79709c2afe6906420bfcfc3000999ddf9e@ec2-23-21-106-145.compute-1.amazonaws.com:14339')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

