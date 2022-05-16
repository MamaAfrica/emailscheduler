from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Compose
from ckeditor.fields import RichTextField
# from django.template.loader import render_to_string
# from django.forms import ValidationError
from django.contrib.auth.models import User
# from .tasks import send_saved_email_task
# from bootstrap_datepicker_plus.widgets import DateTimePickerInput

class CreateUserForm(UserCreationForm):
    username = forms.CharField(error_messages={'unique':'username is already taken'},widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': "JohnDoe"}))
    email = forms.EmailField(
        widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': "johndoe@gmail.com"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': "form-control", 'placeholder': "Password"}))
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': "form-control", 'placeholder': "Confirm Password"}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ComposeForm(ModelForm):
    # user = forms.ModelChoiceField(queryset=User.objects.all())
    To = forms.EmailField()
    cc = forms.EmailField(required=False)
    bcc = forms.EmailField(required=False)
    subject = forms.CharField(max_length=200,required=False)
    body = RichTextField(blank=True,null=True)
    # date_time = forms.DateTimeField()

    # def send_email(self):
    #     body=self.cleaned_data['body']
    #     template=render_to_string('emailtemplate.html',{'body':body})
    #     body=template
    #     return send_saved_email_task.apply_async((self.cleaned_data['To'], self.cleaned_data['subject'], body), countdown=10)
    #     # return send_saved_email_task.delay(self.cleaned_data['To'], self.cleaned_data['subject'], body)

    class Meta:
        model = Compose
        fields = ['To','cc','bcc','subject','body']
        # widgets ={'date_time':DateTimePickerInput}







