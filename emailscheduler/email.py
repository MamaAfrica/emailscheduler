from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.utils.html import strip_tags


def send_saved_email(to, subject, body):
    html_content = render_to_string('emailtemplate.html', {'body': body})
    text_content = strip_tags(html_content)
    msg = EmailMultiAlternatives(subject, text_content, settings.DEFAULT_FROM_EMAIL, [to])
    msg.attach_alternative(html_content, "text/html")
    return msg.send()
