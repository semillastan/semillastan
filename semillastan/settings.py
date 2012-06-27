# Django settings for semillastan project.

import os
ROOT_DIR = os.path.abspath(os.path.dirname(__file__))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Stanley Semilla', 'semillastan@gmail.com'),
)

MANAGERS = ADMINS

TIME_ZONE = 'America/Chicago'
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

USE_I18N = True
USE_L10N = True

MEDIA_ROOT = os.path.join(ROOT_DIR, '..', 'media')
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(ROOT_DIR, '..', 'static')
STATIC_URL = '/static/'

UPLOAD_DIR = 'uploads'
UPLOAD_ROOT = os.path.join(MEDIA_ROOT, UPLOAD_DIR)
UPLOAD_URL = MEDIA_URL + UPLOAD_DIR + '/'

from django.core.files.storage import FileSystemStorage
UPLOAD_STORAGE = FileSystemStorage(location=UPLOAD_ROOT, base_url=UPLOAD_URL)

#ADMIN_MEDIA_PREFIX = '/static/admin/'
ADMIN_MEDIA_PREFIX = STATIC_URL + "grappelli/"
STATICFILES_DIRS = ()

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.DefaultStorageFinder',
    'compressor.finders.CompressorFinder',
)

SECRET_KEY = 'n_h(lvham&amp;=aoh04444+($^05434m84wzxcnhede5*j+#(&amp;xlw'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'semillastan.urls'
WSGI_APPLICATION = 'semillastan.wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(ROOT_DIR, '..', 'templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'grappelli',
    'django.contrib.admin',
    
    'south',
    'imagekit',
    'registration',
    'social_auth',
    'compressor',
    
    'accounts',
    'core',
)

ACCOUNT_ACTIVATION_DAYS = 3
AUTH_PROFILE_MODULE = 'accounts.UserProfile'

AUTHENTICATION_BACKENDS = (
    'social_auth.backends.twitter.TwitterBackend',
    'social_auth.backends.facebook.FacebookBackend',
    'django.contrib.auth.backends.ModelBackend',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.request',
    'django.core.context_processors.static',
    'django.core.context_processors.media',
    'django.contrib.auth.context_processors.auth',
     'social_auth.context_processors.social_auth_by_type_backends',
)

SOCIAL_AUTH_ENABLED_BACKENDS = ('twitter', 'facebook',)

LOGIN_URL          = '/accounts/login/'
LOGIN_REDIRECT_URL = '/accounts/profile/'
LOGIN_ERROR_URL    = '/accounts/login/'

GRAPPELLI_ADMIN_TITLE = 'SemillaStan Site Administrator'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

try:
    from localsettings import *
except ImportError:
    raise ImportError('Please provide your own localsettings.py.\n'
                     'Refer to localsettings.py.template for an example')
