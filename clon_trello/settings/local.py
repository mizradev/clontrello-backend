from .base import *

from decouple import config

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": config('LOCAL_DB_NAME'),
        "USER": config('LOCAL_DB_USER'),
        "PASSWORD": config('LOCAL_DB_PASSWORD'),
        "HOST": "localhost",
        "PORT": "5432",
    }

}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'