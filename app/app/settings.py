
from pathlib import Path
import dj_database_url
import os
from dotenv import load_dotenv

load_dotenv()
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-i-u^$kp#^7tm3j7ns&llg1j^0dx-_30=gz3)c3!3#n9bgk=9gn'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'agenda',
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

ROOT_URLCONF = 'app.urls'

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

WSGI_APPLICATION = 'app.wsgi.application'

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'dbnube',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'PORT': '5432',
        'HOST': 'base-nube.cqzigpaelisx.us-east-2.rds.amazonaws.com',
    }
}



# DATABASES ["default"] = dj_database_url.parse("postgres://lab5_gc4o_user:SNDreeQG4Idf0GUWWXkEE9uUNxEtxDLD@dpg-ckad6nugtj9c73fbn6j0-a.oregon-postgres.render.com/lab5_gc4o")


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


# Configuración para usar Amazon S3 como almacenamiento
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = 'bucket-nube'
AWS_S3_REGION_NAME = 'us-east-2'  # por ejemplo, 'us-west-1'

# Configuración para usar django-storages como backend de almacenamiento
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# Directorio donde se almacenan los archivos estáticos
STATIC_URL = 'https://%s.s3.amazonaws.com/static/' % AWS_STORAGE_BUCKET_NAME

# Directorio donde se almacenan los archivos multimedia
MEDIA_URL = 'https://%s.s3.amazonaws.com/media/' % AWS_STORAGE_BUCKET_NAME

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
STATICFILES_DIRS=(os.path.join(BASE_DIR, 'agenda/static'),)


MEDIA_ROOT = BASE_DIR / "files/fotos"
MEDIA_URL = "/media/"