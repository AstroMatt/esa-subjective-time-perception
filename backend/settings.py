import os
from django.conf.locale.en import formats as en_formats
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT_URLCONF = 'backend.urls'
WSGI_APPLICATION = 'backend.wsgi.application'

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'k$9cmyrlx#2)06(0pb^o&phvqpv^)06mc*9vb($wi3t+++6v=q'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    'localhost',
    'stpa.astrotech.io',
    'time.astrotech.io',
]

# Application definition
INSTALLED_APPS = [
    'grappelli.dashboard',
    'grappelli',
    'import_export',
    # 'django_extensions',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'backend.logger',
    # 'backend.api_v1',
    'backend.api_v2',
]

MIDDLEWARE = [
    # 'django.middleware.cache.UpdateCacheMiddleware',
    # 'django.middleware.locale.LocaleMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'django.middleware.cache.FetchFromCacheMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

if os.environ.get('DATABASE_URL'):
    import dj_database_url
    DATABASES['default'] = dj_database_url.config()

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'frontend'),
]

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, '_media')

en_formats.DATETIME_FORMAT = 'Y-m-d H:i:s.u'
en_formats.DATETIME_INPUT_FORMATS = ['%Y-%m-%d %H:%M:%S.%f']

admin.site.site_header = _('Subjective Time Perception')
admin.site.index_title = _('Control Panel')
admin.site.site_title = _('Subjective Time Perception Control Panel')

GRAPPELLI_ADMIN_TITLE = _('Subjective Time Perception')
GRAPPELLI_INDEX_DASHBOARD = 'backend.dashboard.IndexDashboard'
GRAPPELLI_AUTOCOMPLETE_SEARCH_FIELDS = {
    'auth': {
        'user': ['username__icontains']
    }
}

if os.path.exists('/tmp/memcached.sock'):
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.memcached.PyLibMCCache',
            'LOCATION': '/tmp/memcached.sock',
        }
    }
else:
    CACHES = {
        'default': {
            # 'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
            'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        }
    }
