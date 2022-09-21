"""
Django settings for app project.

Generated by 'django-admin startproject' using Django 3.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

import os
from pathlib import Path
from environs import Env
from garpix_notify.settings import *  # noqa

env = Env()
env.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool('DEBUG', True)

ALLOWED_HOSTS = ['*']

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'solo',
    'ckeditor',
    'fcm_django',
    'user',
    'garpix_notify',
    'app',
    'eqator',
    'channels',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'app.urls'

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

WSGI_APPLICATION = 'app.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('POSTGRES_DB'),
        'USER': env('POSTGRES_USER'),
        'PASSWORD': env('POSTGRES_PASSWORD'),
        'HOST': env('POSTGRES_HOST'),
        'PORT': env.int('POSTGRES_PORT'),
    },
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(BASE_DIR, '..', 'public', 'static')
MEDIA_ROOT = os.path.join(BASE_DIR, '..', 'public', 'media')

TEMPLATES_PATH = os.path.join(BASE_DIR, '..', 'frontend', 'templates')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, '..', 'frontend', 'static'),
]

SITE_ID = 1

LANGUAGE_CODE = 'en'
USE_DEFAULT_LANGUAGE_PREFIX = False

LANGUAGES = (
    ('en', 'English'),
)

# migrations

MIGRATION_MODULES = {
    'garpix_notify': 'app.migrations.garpix_notify',
}

AUTH_USER_MODEL = 'user.User'

# notify events
REGISTRATION_EVENT = 1
REGISTRATION_CALL_CODE = 2
FEEDBACK_EVENT = 3
EXAMPLE_EVENT_1 = 4
EXAMPLE_EVENT_2 = 5
TEST_EVENT_2 = 6

NOTIFY_EVENTS = {
    REGISTRATION_EVENT: {
        'title': 'Register',
    },
    REGISTRATION_CALL_CODE: {
        'title': 'Register call code',
        'text': 'status: {status}, code: {code}, cost: {cost}, balance: {balance}'
    },
    FEEDBACK_EVENT: {
        'title': 'Feeback',
    },
    EXAMPLE_EVENT_1: {
        'title': 'Example 1',
    },
    EXAMPLE_EVENT_2: {
        'title': 'Example 2',
    },
    TEST_EVENT_2: {
        'title': 'TestEvent',
    },
}

CHOICES_NOTIFY_EVENT = [(k, v['title']) for k, v in NOTIFY_EVENTS.items()]

NOTIFY_SMS_URL = "http://sms.ru/sms/send"
NOTIFY_SMS_API_ID = "1234567890"
FCM_DJANGO_SETTINGS = {
    "FCM_SERVER_KEY": "1234567890",
    "APP_VERBOSE_NAME": "Firebase Cloud Messaging",
    "ONE_DEVICE_PER_USER": False,
    "DELETE_INACTIVE_DEVICES": False,
}

CKEDITOR_UPLOAD_PATH = ''

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'width': '100%',
    },
}

# Celery

REDIS_HOST = env('REDIS_HOST', 'localhost')
REDIS_PORT = env.int('REDIS_PORT', 6379)

CELERY_BROKER_URL = f'redis://{REDIS_HOST}:6379/1'
CELERY_RESULT_BACKEND = f'redis://{REDIS_HOST}:6379/2'
# CELERY_RESULT_BACKEND = 'django-db'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
# CELERY_TIMEZONE = TIME_ZONE
# CELERY_TASK_ALWAYS_EAGER = TEST
CELERY_ENABLE_UTC = False
DJANGO_CELERY_BEAT_TZ_AWARE = False

EMAIL_BACKEND = 'garpix_notify.smtp.EmailBackend'

ASGI_APPLICATION = 'app.asgi.application'
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [(REDIS_HOST, REDIS_PORT)],
        },
    },
}

GARPIX_NOTIFY_MIXIN = 'garpix_notify.mixins.notify_mixin.NotifyMixin'
GARPIX_SYSTEM_NOTIFY_MIXIN = 'garpix_notify.mixins.notify_mixin.NotifyMixin'

DEBUG_TOOLBAR = os.getenv('DEBUG_TOOLBAR', False)

if DEBUG_TOOLBAR:
    MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]
    INTERNAL_IPS = ["127.0.0.1"]
    INSTALLED_APPS += ['debug_toolbar']
    DEBUG_TOOLBAR_PANELS = [
        'debug_toolbar.panels.history.HistoryPanel',
        'debug_toolbar.panels.versions.VersionsPanel',
        'debug_toolbar.panels.timer.TimerPanel',
        'debug_toolbar.panels.settings.SettingsPanel',
        'debug_toolbar.panels.headers.HeadersPanel',
        'debug_toolbar.panels.request.RequestPanel',
        'debug_toolbar.panels.sql.SQLPanel',
        'debug_toolbar.panels.staticfiles.StaticFilesPanel',
        'debug_toolbar.panels.templates.TemplatesPanel',
        'debug_toolbar.panels.signals.SignalsPanel',
        'debug_toolbar.panels.logging.LoggingPanel',
        'debug_toolbar.panels.redirects.RedirectsPanel',
        'debug_toolbar.panels.profiling.ProfilingPanel',
    ]

TEST_COVERAGE_RATE = 50
