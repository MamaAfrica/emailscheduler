from django.shortcuts import render, redirect
from .forms import CreateUserForm, ComposeForm
from .models import Compose
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.contrib.auth.forms import UserCreationForm

def signup(request):
    if request.user.is_authenticated:
        return redirect("home")
    else:
        form = CreateUserForm()
        if request.method=="POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data['username']
                messages.success(request, "account successfully created for "+ user)
                return redirect("signin")
            # else:
            #     raise ValueError("username already taken")
        context = {'form':form}
        return render(request, 'signup.html', context)


def signin(request):
    if request.user.is_authenticated:
        return redirect("home")
    else:
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                messages.info(request,"username or password is incorrect")
        return render(request, 'signin.html')


def signout(request):
    logout(request)
    return redirect("signin")

@login_required(login_url="signin")
def emailscheduler(request):
    return render(request, "index.html")

@login_required(login_url="signin")
def compose(request):
    form= ComposeForm()
    if request.method=="POST":
        form=ComposeForm(request.POST)
        form.save()
        return redirect("home")
    else:
        return render(request,'compose.html', {"form":form})

def saved(request,):
    emaillist= Compose.objects.all()
    return render(request, 'saved.html',{"emaillist":emaillist})

def showsaved(request, saved_id):
    saved = Compose.objects.get(pk=saved_id)
    return render(request,'showsaved.html', {'saved':saved})