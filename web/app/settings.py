"""
Django settings for app project.

Generated by 'django-admin startproject' using Django 3.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
SETTINGS_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(SETTINGS_DIR)
def _SETTINGS(p): return os.path.join(SETTINGS_DIR, p)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '6)hqwzih1v02j3*7+df59ymk2)w9emdon7j+4k+!&6h3n=-wxg'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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
        'DIRS': [],
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
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

USE_I18N = True
USE_L10N = True
USE_TZ = True

######
PRJ_APPS = [
    'gpress',
    'api',
    'frontend',
]
PRJ_MIDDLEWARE = [
    'app.middleware.CorsMiddleware',
]
# Static files (https://docs.djangoproject.com/en/3.0/howto/static-files/)
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
LANGUAGE_CODE = 'ja'
TIME_ZONE = 'Asia/Tokyo'
INSTALLED_APPS = INSTALLED_APPS + PRJ_APPS

## API
INSTALLED_APPS += [
    'graphene_django',
    'rest_framework', 'django_filters', 'rest_framework_filters',
    'corsheaders',
]
GRAPHENE = {
    'SCHEMA': 'api.schema.schema'
}

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ('rest_framework_filters.backends.RestFrameworkFilterBackend', ),   # NOQA
}

# CORS: https://github.com/adamchainz/django-cors-headers
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
] + MIDDLEWARE + PRJ_MIDDLEWARE

CORS_ORIGIN_REGEX_WHITELIST = [
    r'https?://[^\.]+:\d+',
    r'https?://localhost:\d+',
    r'http://127.0.0.1:\d+',
]
CORS_ALLOW_CREDENTIALS = True   # CORS_ORIGIN_ALLOW_ALL = True  # No!!!!!
CORS_EXPOSE_HEADERS = [
    'X-CSRFToken', 
    'X-IsAuthenticated', ] 
CORS_PREFLIGHT_MAX_AGE = 10

# CSRF
# https://docs.djangoproject.com/en/3.0/ref/settings/#csrf-trusted-origins
CSRF_TRUSTED_ORIGINS = [
    'localhost:3000',
    '127.0.0.01:3000',
]

FRONTEND_PATH = os.path.join(os.path.dirname(BASE_DIR), 'ui/build')

# Database Routing
if os.path.isfile(_SETTINGS('databases/__init__.py')):
    DATABASE_ROUTERS = ['app.databases.routers.DatabaseRouter']
    from . import databases 
    DATABASES.update(databases.DATABASES)
# Local Settings

if os.path.isfile(_SETTINGS('loggings.py')):
    from .loggings import *    # NOQA

# Local Settings
if os.path.isfile(_SETTINGS('local_settings.py')):
    from .local_settings import *    # NOQA
