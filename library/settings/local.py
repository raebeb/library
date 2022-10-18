from .base import *

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

#TODO: reinstall postgresql

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "dblibrary",
        "USER": "admin_library",
        "PASSWORD": "admin",
        "HOST": "localhost",
        "PORT": "5432"
    }
}
STATIC_URL = "static/"