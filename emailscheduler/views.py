from django.shortcuts import render, redirect
from .forms import CreateUserForm, ComposeForm
from .models import Compose
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .tasks import send_saved_email_task
from datetime import datetime,timedelta
from django.utils import timezone
from django.core.paginator import Paginator
import pytz
import time
from celery.result import AsyncResult
import celery
from django.http import HttpResponse
from celery import uuid
# from django.conf import settings
# from django.core.mail import send_mail
# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm

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
    form = ComposeForm()
    if request.method=="POST":
        form=ComposeForm(request.POST)
        if form.is_valid():
            if 'save' in request.POST:
                form = form.save(commit=False)
                form.user = request.user
                form.draft=True
                form.save()
                return redirect("saved")
            elif 'schedule_send' in request.POST:
                date_time=request.POST['date_time']
                # print(date_time)
                date_time=datetime.fromisoformat(date_time).replace(tzinfo=pytz.UTC)
                # # date_time=datetime.strptime(date_time,'%Y-%m-%d %H:%M').timestamp()
                current = datetime.now()
                unix_timestamp = time.mktime(current.timetuple())
                date_unix = time.mktime(date_time.timetuple())
                date_time= date_unix-unix_timestamp
                print(date_time)
                # date_time=date_time-datetime.now()
                # date_time=int(date_time.total_seconds())

                # date_time = date_time.astimezone(pytz.timezone('UTC'))
                # current = datetime.now(pytz.timezone('UTC'))
                # date_time=abs((date_time - current).total_seconds())
                # print(date_time)
                # sendtime=datetime.now()+ timedelta(seconds=date_time)
                # print(sendtime)
                taskid = uuid()
                send_saved_email_task.apply_async((form.cleaned_data['To'], form.cleaned_data['subject'], form.cleaned_data['body']), countdown=date_time, task_id=taskid)
                # send_saved_email_task.delay(form.cleaned_data['To'], form.cleaned_data['subject'], form.cleaned_data['body'])
                # form.send_email()
                form=form.save(commit=False)
                form.user = request.user
                form.draft = False
                date_time = request.POST['date_time']
                form.date_time = datetime.fromisoformat(date_time)
                form.save()
                # task = AsyncResult(taskid)
                # print(task.state)
                # if task.state == 'PENDING':
                #     data = {
                #         'state': task.state,
                #         # 'progress': task.info.get("progress", 0)
                #     }
                # elif task.state != 'FAILURE':
                #     data = {
                #         'state': task.state,
                #         # 'progress': task.info.get("progress", 0)
                #     }
                # else:
                #     data = {
                #         'state': task.state,
                #         'error': "something went wrong",
                #         # 'progress': task.info.get("progress", 0)
                #     }
                # response = HttpResponse(data)
                # form.send_email()
                return redirect("scheduled")
                # return response
        else:
            return render(request, 'compose.html', {"form": form})
    else:
        return render(request,'compose.html', {"form":form})

def saved(request):
    emaillist= Compose.objects.filter(user=request.user)
    paginator = Paginator(emaillist,5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'saved.html',{"emaillist":emaillist,'page_obj': page_obj})

def showsaved(request, saved_id):
    saved = Compose.objects.get(pk=saved_id)
    print(saved)
    return render(request,'showsaved.html', {'saved':saved})

def delete(request, id):
    instance = Compose.objects.get(id=id)
    instance.delete()
    return redirect('saved')

def scheduled(request):
    emaillist= Compose.objects.filter(draft=False, user=request.user).order_by('-date_time')
    # taskstatus=send_saved_email_task.AsyncResult(send_saved_email_task.request.id).state
    # print(taskstatus)
    paginator=Paginator(emaillist,5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    print(emaillist)
    return render(request, 'scheduled.html',{"emaillist":emaillist,'page_obj': page_obj})

def showscheduled(request, scheduled_id):
    scheduled = Compose.objects.get(pk=scheduled_id)
    print(scheduled)
    return render(request,'showscheduled.html', {'scheduled':scheduled})

