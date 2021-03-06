"""
Django settings for classroomtools project.

import from base

"""

from classroomtools.settings.base import *
from decouple import config
import dj_database_url

DEBUG = False
INSTALLED_APPS += [
    # other apps for production site
]

# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY = config['general']['secretkey']
#SECRET_KEY = config('SECRET_KEY')

ALLOWED_HOSTS = ['*']


# Application definition


# setup email

#WSGI
WSGI_APPLICATION = 'classroomtools.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR,'db.sqlite3'),
        }
    }
db_from_env = dj_database_url.config()

DATABASES['default'].update(db_from_env)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

# compression and caching support from whitenoise
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

