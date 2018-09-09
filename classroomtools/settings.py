"""
Django settings for classroomtools project.

Generated by 'django-admin startproject' using Django 2.0.8.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""


import os
from decouple import config
import dj_database_url
import configparser

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# Read config.ini
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

#use the config lines below if using configparser with .ini file
#config = configparser.ConfigParser()
#config.read(os.path.join(PROJECT_ROOT, 'config.ini'))

# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY = config['general']['secretkey']
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = ['*']





# Application definition

INSTALLED_APPS = [
    'whitenoise.runserver_nostatic',
    'randomizer.apps.ClassroomConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # The following apps are required for allauth:
    #'django.contrib.auth',     -- this is already installed
    'django.contrib.sites',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
        
    #can also include social providers:
]

#allauth settings
SITE_ID = 1
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 2
ACCOUNT_EMAIL_VERIFICATION = 'optional'
ACCOUNT_EMAIL_REQUIRED = 'true'
LOGIN_REDIRECT_URL = "/randomizer/"
ACCOUNT_LOGOUT_REDIRECT_URL = "/accounts/login"

# setup email
#EMAIL_HOST = config['emailconfig']['emailhost']
#EMAIL_HOST_USER = config['emailconfig']['username']
#EMAIL_HOST_PASSWORD = config['emailconfig']['password']
EMAIL_HOST = config('EMAIL_HOST')
EMAIL_HOST_USER = config('EMAIL_USERNAME')
EMAIL_HOST_PASSWORD = config('EMAIL_PASSWORD')
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
EMAIL_PORT = config('EMAIL_PORT', cast=int)
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend' 

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'classroomtools.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        #'DIRS': [],
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # `allauth` needs this from django
                'django.template.context_processors.request',
            ],
        },
    },
]

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',
    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',

)

#WSGI_APPLICATION = 'classroomtools.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME'),
		'USER': config('DB_USER'),
		'PASSWORD': config('DB_PASSWORD'),
		'HOST': config('DB_HOST'),
		'PORT': config('DB_PORT', cast=int),
    }
}

##DATABASES = {
##    'default': {
##        'ENGINE': 'django.db.backends.sqlite3',
##        'NAME': os.path.join(BASE_DIR,'db.sqlite3'),
##        }
##    }
##db_from_env = dj_database_url.config()
##
##DATABASES['default'].update(db_from_env)


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Vancouver'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

# compression and caching support from whitenoise
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

