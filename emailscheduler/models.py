from django.db import models
from ckeditor.fields import RichTextField

class Compose(models.Model):
    To = models.EmailField()
    cc = models.EmailField()
    bcc = models.EmailField()
    subject = models.CharField(max_length=200)
    body = RichTextField()

    def __str__(self):
        return self.subject
