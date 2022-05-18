web: gunicorn emailscheduler.wsgi --log-file -
celery: celery -A emailscheduler worker -l info -c 4