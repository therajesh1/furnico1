"""
Django settings for furnicure project.

Generated by 'django-admin startproject' using Django 5.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""


from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure--hg(ln*9yb0h3$(af9s8=9t@!+&kb9u3aafkb^ovp&%#7sz*#c'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'eco.apps.EcoConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cloudinary',
    'cloudinary_storage',
    'storages',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'furnicure.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],
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

WSGI_APPLICATION = 'furnicure.wsgi.application'

import cloudinary
import cloudinary.uploader
import cloudinary.api

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'djvsbqfwv',
    'API_KEY': '715889147158576',
    'API_SECRET': 'P5uZ0P-Si_Wp1gbbcD423Cu2lWs',
    'SECURE_URL': True,  # Ensures HTTPS

}

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# Optional: Set media URL if you want to access via a CDN
MEDIA_URL = 'https://res.cloudinary.com/djvsbqfwv/'

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_HOST_USER = 'therajeshchheda@gmail.com'
# EMAIL_HOST_PASSWORD = 'your-email-password'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'fcure',
#         'USER': 'root',
#         'PASSWORD': '123abcd123',
#         'HOST': '127.0.0.1',  # Or your database server's IP address
#         'PORT': '3306',       # Default MySQL port
#     }
# }
# from mongoengine import connect

# connect('furnicure', host='mongodb://localhost/furnicure')
# DATABASES = {
#     'default': {
#         'ENGINE': 'djongo',
#         'NAME': 'furnico',  # Your MongoDB database name
#         'ENFORCE_SCHEMA': False,        # Disable strict schema enforcement
#         'CLIENT': {
#             'host': 'mongodb://localhost:27017',  # Replace with your MongoDB URL
#             # 'username': 'your_username',         # Optional
#             # 'password': 'your_password',         # Optional
#             'authSource': 'admin',               # Default auth source
#         }
#     }
# }
# import pymongo
DATABASES = {
     'default': {
         'ENGINE': 'django.db.backends.postgresql',
         'NAME': 'railway',
         'USER': 'postgres',
         'PASSWORD': 'DjMsDKYbfMFSaaJRjLxqNAMBSArDSYmP',
         'HOST': 'monorail.proxy.rlwy.net',
         'PORT': '16342'
        
     }
}

# pymongo.MongoClient().close = lambda: None

import sys
import types

sys.modules['cgi'] = types.ModuleType('cgi')


from django.http import HttpResponsePermanentRedirect

class RedirectToWwwMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.get_host().startswith('www'):
            return HttpResponsePermanentRedirect(
                f"https://www.{request.get_host()}{request.get_full_path()}"
            )
        return self.get_response(request)


TIME_ZONE = 'Asia/Kolkata'  # Replace with your preferred timezone

# settings.py
USE_TZ = True  # Ensures timezone-aware datetimes

# DATABASES = {
#      'default': {
#          'ENGINE': 'django.db.backends.postgresql',
#          'NAME': 'railway',
#          'USER': 'postgres',
#          'PASSWORD': 'LddtqWSHcfoXMGqayEXmoQDlVmikklpR',
#          'HOST': 'postgres.railway.internal',
#          'PORT': '5432'
        
#      }
# }
# import os

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': os.getenv('DB_NAME'),
#         'USER': os.getenv('DB_USER'),
#         'PASSWORD': os.getenv('DB_PASSWORD'),
#         'HOST': os.getenv('DB_HOST'),
#         'PORT': os.getenv('DB_PORT'),
#     }
# }
import os
from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env file

# google_credentials = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")

# # Add Google Drive settings
# GOOGLE_DRIVE_STORAGE_JSON_KEY_FILE = 'google_credentials/your_credentials_file.json'  # Replace with your file's actual path
# GOOGLE_DRIVE_STORAGE_FOLDER_ID = 'your-google-drive-folder-id'  # (Optional) If you want to store the files in a specific folder

# Set up default file storage to Google Drive
GOOGLE_DRIVE_STORAGE = 'eco.storages.GoogleDriveStorage'

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# MEDIA_URL = '/media/'
# MEDIA_ROOT = BASE_DIR / 'media'

# STATIC_URL = '/static/'
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

# STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



# STATIC_URL = 'static/'

STATICFILES_DIRS = [
    BASE_DIR / "static",
    
]

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
import os
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Add this if you have media files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'mediafiles')
import os

BASE_DIR = Path(__file__).resolve().parent.parent

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'mediafiles')  # Ensure this is correct and points to the right folder


# import os

# # Static files (CSS, JavaScript, Images)
# STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # For collected static files (used in production)
# STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]  # Development static files directory

# # Media files (User-uploaded content)
# MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  # Folder where uploaded files are stored

