"""emailscheduler URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('tz_detect/', include('tz_detect.urls')),
    path('admin/', admin.site.urls),
    path("", views.emailscheduler, name="home"),
    path("signup/", views.signup, name="signup"),
    path("signin/", views.signin, name="signin"),
    path("signout/", views.signout, name="signout"),
    path("compose/", views.compose, name="compose"),
    path("saved/", views.saved, name="saved"),
    path("showsaved/<saved_id>/", views.showsaved, name="showsaved"),
    path("delete/<id>/", views.delete, name="delete"),
    path("scheduled/", views.scheduled, name="scheduled"),
    path("showsaved/<scheduled_id>/", views.showscheduled, name="showscheduled"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
