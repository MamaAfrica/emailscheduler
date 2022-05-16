# from django.template import Context
from django.template.loader import render_to_string
from django.core.mail import send_mail, EmailMultiAlternatives
from django.conf import settings
from django.utils.html import strip_tags
# from django.template import Template


def send_saved_email(to, subject, body):
    html_content = render_to_string('emailtemplate.html', {'body': body})
    text_content = strip_tags(html_content)
    msg = EmailMultiAlternatives(subject, text_content, settings.DEFAULT_FROM_EMAIL, [to])
    msg.attach_alternative(html_content, "text/html")
    return msg.send()
    # email_subject = subject
    # html_message = render_to_string('emailtemplate.html', {'body': body})
    # plain_message = strip_tags(html_message)
    # # from_email = 'From <from@example.com>'
    # # to = 'to@example.com'
    #
    # email_body = plain_message
    # return send_mail(subject=email_subject, html_message=html_message, from_email=settings.DEFAULT_FROM_EMAIL,
    #                  recipient_list=[To], message=email_body, fail_silently=False)
