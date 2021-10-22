
from bugtail.settings.base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-gn^algytp%kr-hpxs8m&kr7-l@-f+2#%h0e4-_d-8^)$q0#28u'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

DATABASES['default'] = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'bugtail.db',
    }


STATIC_URL = '/static/'
STATIC_ROOT = Path.cwd().joinpath(BASE_DIR).joinpath('assets')
STATICFILES_DIRS = [
    Path.cwd().joinpath(BASE_DIR).joinpath('bugtail/assets'),
]


MEDIA_URL = '/media/'
MEDIA_ROOT = Path.cwd().joinpath(BASE_DIR).joinpath('media')

