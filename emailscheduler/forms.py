from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Compose
from ckeditor.fields import RichTextField
from django.forms import ValidationError
from django.contrib.auth.models import User


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
    To = forms.EmailField()
    cc = forms.EmailField()
    bcc = forms.EmailField()
    subject = forms.CharField(max_length=200)
    body = RichTextField()
    class Meta:
        model = Compose
        fields = "__all__"




