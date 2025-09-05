"""
Django settings for dhirajhouses project.
Updated for Django 5.2 and modern best practices.
"""

from pathlib import Path
import os
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# --- Core Security Settings (Loaded from Environment) ---

# SECURITY WARNING: keep the secret key used in production secret!
# Load the secret key from an environment variable.
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'default-insecure-key-for-development-only')

# SECURITY WARNING: don't run with debug turned on in production!
# Load DEBUG setting from an environment variable (defaults to True for development).
DEBUG = os.getenv('DJANGO_DEBUG', 'True') == 'True'

# In development with Docker, '*' is acceptable. In production, be specific.
# e.g., ALLOWED_HOSTS = os.getenv('DJANGO_ALLOWED_HOSTS', '127.0.0.1,localhost').split(',')
ALLOWED_HOSTS = ["*"]

# --- Application Definition ---

INSTALLED_APPS = [
    "pages.apps.PagesConfig",
    "listings.apps.ListingsConfig",
    "realtors.apps.RealtorsConfig",
    "accounts.apps.AccountsConfig",
    "contacts.apps.ContactsConfig",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.humanize",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "dhirajhouses.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / 'templates'], # Use modern pathlib and a project-level templates dir
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "dhirajhouses.wsgi.application"


# --- Database Configuration ---

# Reads database configuration from a single DATABASE_URL environment variable for flexibility.
DATABASES = {
    'default': dj_database_url.config(
        # Default to a local SQLite file if DATABASE_URL is not set
        default=f'sqlite:///{BASE_DIR / "db.sqlite3"}'
    )
}


# --- Password Validation ---

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


# --- Internationalization ---

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True


# --- Static & Media Files ---

STATIC_URL = "/static/"
# Directory where Django will collect all static files for production.
STATIC_ROOT = BASE_DIR / 'staticfiles'
# Additional locations the staticfiles app will traverse for development.
STATICFILES_DIRS = [
    BASE_DIR / 'dhirajhouses/static',
]
# URL that handles the media served from MEDIA_ROOT.
MEDIA_URL = '/media/'
# Absolute filesystem path to the directory that will hold user-uploaded files.
MEDIA_ROOT = BASE_DIR / 'media'


# --- Default Primary Key Field Type ---

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# --- Messages Configuration ---

from django.contrib.messages import constants as messages
MESSAGE_TAGS = {
    messages.ERROR: 'danger',
}


# --- Email Configuration (Loaded from environment variables) ---
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.getenv('EMAIL_HOST', 'smtp.gmail.com')
EMAIL_PORT = int(os.getenv('EMAIL_PORT', 587))
EMAIL_USE_TLS = os.getenv('EMAIL_USE_TLS', 'True') == 'True'
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
