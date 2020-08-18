"""
Django settings for demo project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from __future__ import unicode_literals

import os
from django.utils.translation import gettext_lazy as _
from os.path import join
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '^)gds%1$%i!w$u7&_h2j$8od20#h$li(9(qu)nt7_%48hkzmmu'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'star_ratings',

    'demo.app',
)

MIDDLEWARE = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'demo.urls'

WSGI_APPLICATION = 'demo.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

LANGUAGES = [
  ('de', _('German')),
  ('en', _('English')),
  ('es', _('Spanish')),
  ('eu', _('Basque')),
  ('fr', _('French')),
  ('pt-BR', _('Portuguese (Brazil)')),
  ('ru', _('Russian')),
]

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = join(BASE_DIR, 'static_root')

MEDIA_URL = '/media/'
MEDIA_ROOT = join(BASE_DIR, 'media')

# Additional locations of static files
STATICFILES_DIRS = [
    join(BASE_DIR, 'static'),
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': (
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.template.context_processors.request',
                'django.contrib.messages.context_processors.messages',
            )
        }
    }
]

# Django Star Ratings System
# https://django-star-ratings.readthedocs.io/

# To change the number of rating stars, defaults to 5
STAR_RATINGS_RANGE = 5

# To allow uses to delete a rating via a clear button, defaults to False
STAR_RATINGS_CLEARABLE = False

# To allow uses anonymus to do a rating, defaults to False
STAR_RATINGS_ANONYMOUS = False

# To prohibit users from altering their ratings set, defaults to True
STAR_RATINGS_RERATE = True
STAR_RATINGS_RERATE_SAME_DELETE = False

# To change the star icon height, defaults to 32
STAR_RATINGS_STAR_HEIGHT = 32

# To set the same value from the star icon height to the star icon width, defaults the same STAR_RATINGS_STAR_HEIGHT
STAR_RATINGS_STAR_WIDTH = STAR_RATINGS_STAR_HEIGHT

# To change the star icon path, defaults to 'star-ratings/images/stars.png'
STAR_RATINGS_STAR_SPRITE = 'star-ratings/images/stars.png'

# To override the 'object_id' field on the 'Rating' model to a reasonable value for your new pk field, defaults to a digit
STAR_RATINGS_OBJECT_ID_PATTERN = r'\d+'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'stream': {
            'level': 'ERROR',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['stream'],
            'level': 'ERROR',
            'propagate': True,
        },
    },
}
