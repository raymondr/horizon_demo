import logging
import os
import sys

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))

DEBUG = False
TEMPLATE_DEBUG = DEBUG

SECRET_KEY = 'OMG SO SECRET!!!!!'

OPENSTACK_KEYSTONE_BACKEND = {
    'name': 'native',
    'can_edit_user': True
}

HORIZON_CONFIG = {
    'dashboards': ('nova', 'syspanel', 'visualizations', 'settings',),
    'default_dashboard': 'nova',
    'user_home': 'demo_dashboard.views.user_home',
    'customization_module': 'demo_dashboard.overrides'
}

SITE_ID = 1
SITE_BRANDING = 'Demo Dashboard'
SITE_NAME = 'demo'
ENABLE_VNC = True

LOGIN_URL = '/auth/login'
LOGIN_REDIRECT_URL = '/'

MEDIA_ROOT = os.path.abspath(os.path.join(ROOT_PATH, '..', 'media'))
MEDIA_URL = '/media/'
STATIC_ROOT = os.path.abspath(os.path.join(ROOT_PATH, '..', 'static'))
STATIC_URL = '/static/'

ROOT_URLCONF = 'demo_dashboard.urls'

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'horizon.middleware.HorizonMiddleware',
    'django.middleware.locale.LocaleMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.contrib.messages.context_processors.messages',
    'horizon.context_processors.horizon',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader'
)

TEMPLATE_DIRS = (
    os.path.join(ROOT_PATH, 'templates'),
)

STATICFILES_DIRS = (
    os.path.join(ROOT_PATH, 'static'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

INSTALLED_APPS = (
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'horizon',
    'horizon.dashboards.nova',
    'horizon.dashboards.syspanel',
    'horizon.dashboards.settings',
    'demo_dashboard',
    'demo_dashboard.dashboards.visualizations',
)

MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'

# Using the cookie-based session storage
SESSION_ENGINE = 'django.contrib.sessions.backends.signed_cookies'
SESSION_COOKIE_HTTPONLY = True
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SESSION_COOKIE_SECURE = False

# Send email to the /dev/null.
EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'

TIME_ZONE = None
USE_I18N = True

OPENSTACK_KEYSTONE_DEFAULT_ROLE = 'Member'

try:
    from local.local_settings import *
except ImportError:
    logging.warning("No local_settings file found.")
