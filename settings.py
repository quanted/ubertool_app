"""
Django settings for UberDjango project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

import os, sys
import secret


# Get machine IP address
MACHINE_ID = "developer"

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

# Define ENVIRONMENTAL VARIABLES for project (replaces the app.yaml)
os.environ.update({
    'UBERTOOL_BATCH_SERVER': 'http://uberrest-topknotmeadows.rhcloud.com/',
    'UBERTOOL_MONGO_SERVER': 'http://uberrest-topknotmeadows.rhcloud.com',
    'UBERTOOL_SECURE_SERVER': 'http://uberrest-topknotmeadows.rhcloud.com',   
    'UBERTOOL_REST_SERVER': 'http://localhost:7777',                         # Local REST server
    #'UBERTOOL_REST_SERVER': 'http://54.83.18.251:80',                      # Tao's EC2 REST server 
    #'UBERTOOL_REST_SERVER': 'http://54.210.118.56'                         # EB Pilot REST server
    # 'UBERTOOL_REST_SERVER': 'http://'                           # New EB Pilot REST server
    'REST_SERVER_8': 'http://134.67.114.8',  # 'http://localhost:64399'
    'PROJECT_PATH': PROJECT_ROOT,
    'SITE_SKIN': 'EPA',                          # Leave empty ('') for default skin, 'EPA' for EPA skin
    'CONTACT_URL': 'https://www.epa.gov/research/forms/contact-us-about-epa-research',

    'CTS_EPI_SERVER': 'http://localhost:55342',
    'CTS_EFS_SERVER': 'http://ca-test-1.cloudapp.net',
    'CTS_JCHEM_SERVER': 'http://ca-test-1.cloudapp.net',
    'CTS_SPARC_SERVER': 'http://204.46.160.69:8080',
    'CTS_TEST_SERVER': ''

})

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = secret.SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = [
    '.ubertool.org',
    '.ubertool.org.',
    'localhost',
    '127.0.0.1'
]

ADMINS = (
    ('Ubertool Dev Team', 'ubertool-dev@googlegroups.com')
)

APPEND_SLASH = True

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_ROOT, 'templates').replace('\\','/'),
)

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

# Application definition

INSTALLED_APPS = (
    # 'django.contrib.admin',
    # 'django.contrib.auth',
    #'django.contrib.contenttypes',
    # 'django.contrib.sessions',
    # 'django.contrib.messages',
    'django.contrib.staticfiles',
    #'mod_wsgi.server',  # Only needed for mod_wsgi express (Python driver for Apache) e.g. on the production server
    'docs',
    'api',
    'models.ore',
    'models.hwbi',
    'cts_api'
    # 'rest_framework_swagger'
)

MIDDLEWARE_CLASSES = (
    # 'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    # 'django.contrib.auth.middleware.AuthenticationMiddleware',
    # 'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'urls'

WSGI_APPLICATION = 'wsgi_local.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_ROOT, 'db.sqlite3'),
    }
}

# Authentication
AUTH = False
LOGIN_URL = '/ubertool/login'
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

# Setups databse-less test runner (Only needed for running test)
#TEST_RUNNER = 'testing.DatabaselessTestRunner'

# CACHE Setup - required to run Django "sessions" without a database

# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
#         'LOCATION': 'unique-snowflake'
#     }
# }
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/New_York'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

STATIC_URL = '/static/'

# print 'BASE_DIR = %s' %BASE_DIR
# print 'PROJECT_ROOT = %s' %PROJECT_ROOT

# Path to Sphinx HTML Docs
# http://django-docs.readthedocs.org/en/latest/

DOCS_ROOT = os.path.join(PROJECT_ROOT, 'docs', '_build', 'html')

DOCS_ACCESS = 'public'

# Log to console in Debug mode
if DEBUG:
    import logging
    logging.basicConfig(
        level = logging.DEBUG,
        format = '%(asctime)s %(levelname)s %(message)s',
    )
