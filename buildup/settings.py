import os
import dj_database_url
ROOT_URLCONF = 'buildup.urls'
WSGI_APPLICATION = 'buildup.wsgi.application'
SECRET_KEY = os.environ.get('DJANGO_SECRET', 'sekret')
DEBUG = True
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, "buildup/templates"),
)
DATABASES = { 'default': dj_database_url.config() }
INSTALLED_APPS = (
    'buildup',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
)
LOGIN_REDIRECT_URL = '/facts/'
LOGIN_URL='/login/'
LOGOUT_URL='/logout/'
