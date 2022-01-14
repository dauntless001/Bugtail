from bugtail.settings.base import *
from bugtail.helpers.email_helper import *
from bugtail.settings.packages.aws import *
import os, dj_database_url

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os,os.getenv('DEBUG', 'False') == 'True'

INSTALLED_APPS.append("storages")

MIDDLEWARE.insert(2, "whitenoise.middleware.WhiteNoiseMiddleware")

DATABASES['default'] = dj_database_url.parse(url=os.getenv('DATABASE_URL'), conn_max_age=600)

STATIC_URL = '/static/'
STATIC_ROOT = Path.cwd().joinpath(BASE_DIR).joinpath('assets')
STATICFILES_DIRS = [
    Path.cwd().joinpath(BASE_DIR).joinpath('bugtail/assets'),
]


MEDIA_URL = '/media/'
MEDIA_ROOT = Path.cwd().joinpath(BASE_DIR).joinpath('media')

#Email Backend
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'