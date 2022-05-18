web: gunicorn emailscheduler.wsgi --log-file -
celery: celery worker -A emailscheduler -l info -c 4