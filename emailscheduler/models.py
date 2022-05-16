from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
# from .tasks import send_saved_email_task
class Compose(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="emaillist", null=True)
    To = models.EmailField()
    cc = models.EmailField(blank=True, null=True)
    bcc = models.EmailField(blank=True, null=True)
    subject = models.CharField(max_length=200, blank=True, null=True)
    body = RichTextField(blank=True, null=True)
    date_time = models.DateTimeField(blank=True, null=True)
    draft = models.BooleanField(default=True)

    def __str__(self):
        return self.subject

