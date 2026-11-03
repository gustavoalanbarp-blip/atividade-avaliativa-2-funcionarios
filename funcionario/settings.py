from pathlib import Path
import os
from django.core.management.utils import get_random_secret_key

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY') or get_random_secret_key()
DEBUG = True  # Projeto didático: executar apenas localmente.
ALLOWED_HOSTS = ['localhost', '127.0.0.1', '[::1]']
INSTALLED_APPS = [
    'django.contrib.admin', 'django.contrib.auth', 'django.contrib.contenttypes',
    'django.contrib.sessions', 'django.contrib.messages', 'django.contrib.staticfiles',
    'django_bootstrap5', 'app',
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
ROOT_URLCONF = 'funcionario.urls'
TEMPLATES = [{'BACKEND': 'django.template.backends.django.DjangoTemplates',
              'DIRS': [], 'APP_DIRS': True,
              'OPTIONS': {'context_processors': [
                  'django.template.context_processors.request',
                  'django.contrib.auth.context_processors.auth',
                  'django.contrib.messages.context_processors.messages']}}]
WSGI_APPLICATION = 'funcionario.wsgi.application'
DB_PASSWORD = os.environ.get('DB_PASSWORD', '')
# Arquivo local opcional, ignorado pelo Git, para a senha do seu MySQL.
try:
    from .config_local import DB_PASSWORD
except ModuleNotFoundError as exc:
    if exc.name != 'funcionario.config_local':
        raise
DATABASES = {'default': {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': os.environ.get('DB_NAME', 'funcionarios'),
    'USER': os.environ.get('DB_USER', 'root'),
    'PASSWORD': DB_PASSWORD,
    'HOST': os.environ.get('DB_HOST', '127.0.0.1'),
    'PORT': os.environ.get('DB_PORT', '3306'),
    'OPTIONS': {'charset': 'utf8mb4', 'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"},
}}
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_TZ = True
STATIC_URL = 'static/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
