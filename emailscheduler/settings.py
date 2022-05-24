"""
Django settings for emailscheduler project.

Generated by 'django-admin startproject' using Django 4.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
import django_heroku
from celery.schedules import crontab
import django


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-tde8mk@7j7joc*)=g42injoab6ow8ryk#t(2m=f2h3u=t)t=z)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['ec2-23-21-106-145.compute-1.amazonaws.com','*']

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.zoho.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'admin@mimigrace.xyz'
EMAIL_HOST_PASSWORD = 'Mimigrace@11'
DEFAULT_FROM_EMAIL = 'admin@mimigrace.xyz'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'bootstrap4',
    'bootstrap5',
    'emailscheduler',
    'ckeditor',
    'django_celery_results',
    # 'celery_progress',
    'tz_detect',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'tz_detect.middleware.TimezoneMiddleware',
]

ROOT_URLCONF = 'emailscheduler.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'emailscheduler.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

STATICFILES_DIRS = [
    BASE_DIR / "static",
]
# STATIC_ROOT = "static"
# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
django_heroku.settings(locals())

#CELERY SETTINGS
# CELERY_BROKER_URL = 'amqps://sbvmzyqm:lZ5uSs5CS1qdVDPJyi9g3J9Z8n-ExmpR@shark.rmq.cloudamqp.com/sbvmzyqm'
# CELERY_BROKER_URL = 'amqp://guest:guest@localhost:5672//'
CELERY_BROKER_URL = 'redis://:pb5f0320b5e776373194182c60862bc79709c2afe6906420bfcfc3000999ddf9e@ec2-23-21-106-145.compute-1.amazonaws.com:14339'
# CELERY_RESULT_BACKEND = 'django-db'
CELERY_RESULT_BACKEND = 'redis://:pb5f0320b5e776373194182c60862bc79709c2afe6906420bfcfc3000999ddf9e@ec2-23-21-106-145.compute-1.amazonaws.com:14339'
# CELERY_CACHE_BACKEND = 'django-cache'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'
CELERY_TIMEZONE = 'UTC'
CELERY_ENABLE_UTC = True

# CELERY_BEAT_SCHEDULE = {
# 'send_saved_email_task': {
# 'task': 'tasks.send_saved_email_task',
# 'schedule': crontab(minute='*/2')
# }
# }