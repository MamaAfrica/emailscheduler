# from __future__ import absolute_import, unicode_literals
from celery import shared_task
#imports needed for the functions
# from django.conf import settings
# from django.core.mail import EmailMultiAlternatives
# from django.template.loader import get_template
# from .models import *
# from django.contrib.auth.models import User
# from users.models import *
from celery.utils.log import get_task_logger
from .email import send_saved_email
from celery.result import AsyncResult

logger = get_task_logger(__name__)


@shared_task(name="send_saved_email_task")
def send_saved_email_task(To, subject, body):
    logger.info("Super nice scheduled successfully")
    status=send_saved_email_task.AsyncResult(send_saved_email_task.request.id).state
    print(status)
    return (send_saved_email(To,subject,body), status)
    #     #Logic to send an email here ........


# send_saved_email_task.AsyncResult(send_saved_email_task.request.id).state














# def scheduledTask():
#     #Get Subscriptions
#     notifications = JobNotifi.objects.all()
#     for nx in notifications:
#         if nx.status == 'ACTIVE':
#             selection = nx.subscribed_category
# the_company = Company.objects.get(uniqueId='139260d2')
#             jobs = Jobs.objects.filter(company=the_company, category__title__contains=selection)[:3]
# subject = '[Careers Portal] Weekly Job Notifications'
# email_jobs = {
#             "title": "Job Notifications from Careers Portal",
#             "shortDescription": "Thank you for subscribing to Careers Portal, job notifications. For more jobs visit https://careers-portal.co.za",
#             "subtitle": "Careers Portal - The latest job opportunities, updated weekly",
#             "jobs": jobs
#             }
# sendEmail(email_jobs, subject, [nx.subscribed_user.email])