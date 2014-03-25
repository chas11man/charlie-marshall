"""
Django settings for charlie_marshall project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

# Static asset configuration
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '%18cq#^_=8a$mvan--^mjbxh)ri=xky0%gjw$7rt@&(mf4_*4p'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['.charlie-marshall.com', '.charlie-marshall.herokuapp.com', 'charlie-marshall.com', 'localhost']

# Application definition

INSTALLED_APPS = (
    'django_admin_bootstrapped.bootstrap3',
    'django_admin_bootstrapped',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 3rd party
    'django_extensions',
    'bootstrap3',
    'south',
    'storages',
    'photologue',
    'tinymce',
    'django_s3_collectstatic',
    # apps
    'polls',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'charlie_marshall.urls'

WSGI_APPLICATION = 'charlie_marshall.wsgi.application'

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages'
)

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dauvgseh6hsddm',
        'USER': 'qatgkxjvykoncu',
        'PASSWORD': 'xvy342f6zd43NtiiVoez0bwaZV',
        'HOST': 'ec2-23-21-101-129.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

SHELL_PLUS = 'bpython'

# Parse database configuration from $DATABASE_URL
import dj_database_url

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

AWS_BUCKET_NAME = os.environ['AWS_BUCKET_NAME']
AWS_STORAGE_BUCKET_NAME = AWS_BUCKET_NAME
AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
AWS_PRELOAD_METADATA = True
DEFAULT_FILE_STORAGE = 'charlie_marshall.helpers.MediaRootS3BotoStorage'
STATICFILES_STORAGE = 'charlie_marshall.helpers.StaticRootS3BotoStorage'
STATIC_URL = 'http://static.charlie-marshall.com/static/'
MEDIA_URL = 'http://static.charlie-marshall.com/media/'
#MEDIA_ROOT = ''
STATIC_ROOT = ''

TINYMCE_DEFAULT_CONFIG = {
    'theme': "advanced",
    'cleanup_on_startup': True,
    'custom_undo_redo_levels': 10,
}
TINYMCE_JS_ROOT = STATIC_URL + 'tiny_mce/'
TINYMCE_JS_URL = TINYMCE_JS_ROOT + 'tiny_mce.js'
