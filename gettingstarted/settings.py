"""
Django settings for gettingstarted project, on Heroku. For more info, see:
https://github.com/heroku/heroku-django-template

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

import os
import dj_database_url


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: change this before deploying to production!
SECRET_KEY = 'i+acxn5(akgsn!sr4^qgf(^m&*@+g1@u^t@=8s@axc41ml*f=s'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Application definition

INSTALLED_APPS = (
    'csc510project.apps.Csc510ProjectConfig',
    'rest_framework',
    #'social_auth',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

EMAIL_HOST = "smtp.gmail.com"
EMAIL_HOST_USER = "csc510project@gmail.com"
EMAIL_HOST_PASSWORD = "1#csc510project#1"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER


# AUTHENTICATION_BACKENDS = (
#     'social_auth.backends.twitter.TwitterBackend',
#     'social_auth.backends.facebook.FacebookBackend',
#     'social_auth.backends.google.GoogleOAuthBackend',
#     'social_auth.backends.google.GoogleOAuth2Backend',
#     'social_auth.backends.google.GoogleBackend',
#     'social_auth.backends.yahoo.YahooBackend',
#     'social_auth.backends.browserid.BrowserIDBackend',
#     'social_auth.backends.contrib.linkedin.LinkedinBackend',
#     'social_auth.backends.contrib.disqus.DisqusBackend',
#     'social_auth.backends.contrib.livejournal.LiveJournalBackend',
#     'social_auth.backends.contrib.orkut.OrkutBackend',
#     'social_auth.backends.contrib.foursquare.FoursquareBackend',
#     'social_auth.backends.contrib.github.GithubBackend',
#     'social_auth.backends.contrib.vk.VKOAuth2Backend',
#     'social_auth.backends.contrib.live.LiveBackend',
#     'social_auth.backends.contrib.skyrock.SkyrockBackend',
#     'social_auth.backends.contrib.yahoo.YahooOAuthBackend',
#     'social_auth.backends.contrib.readability.ReadabilityBackend',
#     'social_auth.backends.contrib.fedora.FedoraBackend',
#     'social_auth.backends.OpenIDBackend',
#     'django.contrib.auth.backends.ModelBackend',
# )

# AUTH_USER_MODEL = "csc510project.CustomUser"

TWITTER_CONSUMER_KEY         = ''
TWITTER_CONSUMER_SECRET      = ''
FACEBOOK_APP_ID              = ''
FACEBOOK_API_SECRET          = ''
LINKEDIN_CONSUMER_KEY        = ''
LINKEDIN_CONSUMER_SECRET     = ''
ORKUT_CONSUMER_KEY           = ''
ORKUT_CONSUMER_SECRET        = ''
GOOGLE_CONSUMER_KEY          = ''
GOOGLE_CONSUMER_SECRET       = ''
GOOGLE_OAUTH2_CLIENT_ID      = ''
GOOGLE_OAUTH2_CLIENT_SECRET  = ''
FOURSQUARE_CONSUMER_KEY      = ''
FOURSQUARE_CONSUMER_SECRET   = ''
VK_APP_ID                    = ''
VK_API_SECRET                = ''
LIVE_CLIENT_ID               = ''
LIVE_CLIENT_SECRET           = ''
SKYROCK_CONSUMER_KEY         = ''
SKYROCK_CONSUMER_SECRET      = ''
YAHOO_CONSUMER_KEY           = ''
YAHOO_CONSUMER_SECRET        = ''
READABILITY_CONSUMER_SECRET  = ''
READABILITY_CONSUMER_SECRET  = ''

# Setup login URLs:

LOGIN_URL          = '/login-form/'
LOGIN_REDIRECT_URL = '/logged-in/'
LOGIN_ERROR_URL    = '/login-error/'
# Check Django documentation at Login URL and Login redirect URL

# If a custom redirect URL is needed that must be different to LOGIN_URL, define the setting:

SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/another-login-url/'
# A different URL could be defined for newly registered users:

SOCIAL_AUTH_NEW_USER_REDIRECT_URL = '/new-users-redirect-url/'
# or for newly associated accounts:

SOCIAL_AUTH_NEW_ASSOCIATION_REDIRECT_URL = '/new-association-redirect-url/'
# or for account disconnections:

SOCIAL_AUTH_DISCONNECT_REDIRECT_URL = '/account-disconnected-redirect-url/'
# Users will be redirected to LOGIN_ERROR_URL in case of error or user cancellation on some backends. This URL can be override by this setting:

SOCIAL_AUTH_BACKEND_ERROR_URL = '/new-error-url/'
# Configure authentication and association complete URL names to avoid possible clashes:

SOCIAL_AUTH_COMPLETE_URL_NAME  = 'socialauth_complete'
SOCIAL_AUTH_ASSOCIATE_URL_NAME = 'socialauth_associate_complete'
# Inactive users can be redirected to a different page if this setting is defined:

SOCIAL_AUTH_INACTIVE_USER_URL = '...'

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'gettingstarted.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR+'/csc510project/static/'],
        'APP_DIRS': True,
        'OPTIONS': {
            'debug': True,
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'gettingstarted.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Update database configuration with $DATABASE_URL.
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
)

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/
#STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

