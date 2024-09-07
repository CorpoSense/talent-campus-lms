from pathlib import Path
from datetime import timedelta
from dotenv import load_dotenv
import os 
import environ
# Initialise environment variables
env = environ.Env()
environ.Env.read_env()

EMAIL_BACKEND=env("EMAIL_BACKEND")
EMAIL_HOST=env("EMAIL_HOST")
EMAIL_PORT=env("EMAIL_PORT")
EMAIL_USE_TLS=env("EMAIL_USE_TLS")
EMAIL_HOST_USER=env("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD=env("EMAIL_HOST_PASSWORD")
DEFAULT_FROM_EMAIL=EMAIL_HOST_USER
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-5r9d^nm%@wv--ufn8*1u0=vr4#lv086vmry%8btom1cbua!q^='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework_simplejwt',
    'corsheaders',
    'authApi',
    'lms'
]
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # Comment out CSRF middleware to check if it's causing the issue
     'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
ROOT_URLCONF = 'api.urls'

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

WSGI_APPLICATION = 'api.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'


DEBUG=True

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(hours=2),  # Set the access token lifetime
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),  # Set the refresh token lifetime
    'ROTATE_REFRESH_TOKENS': False,  # Whether to rotate refresh tokens on each use
    'BLACKLIST_AFTER_ROTATION': True,  # Blacklist old refresh tokens after rotation
    'UPDATE_LAST_LOGIN': False,  # Update the user's last login field when they obtain a new token
}


if __import__('os').environ.get('GITPOD_WORKSPACE_URL'):
    try:
        gp = __import__('subprocess').run(["gp", "url", "8000"], capture_output=True, text=True)
        if gp.returncode == 0 and gp.stdout:
            ALLOWED_HOSTS += [gp.stdout.strip().split('//', 1)[-1]]
    except:
        ALLOWED_HOSTS += ['*']


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
CORS_ALLOW_ALL_ORIGINS = True  # Allow all origins for testing purposes

# Alternatively, if you need to be more restrictive:
CORS_ALLOWED_ORIGINS = [
    "https://8000-corposense-talentcampus-0wid12991xq.ws-eu115.gitpod.io",
]

CSRF_TRUSTED_ORIGINS = [
    'https://8000-corposense-talentcampus-0wid12991xq.ws-eu115.gitpod.io',
    # Add other trusted origins if needed
]

PASSWORD_RESET_TIMEOUT = 60 * 60 * 24