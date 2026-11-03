# Somente teste automatizado sem servidor MySQL. Não usar na apresentação.
from .settings import *
DATABASES = {'default': {'ENGINE': 'django.db.backends.sqlite3', 'NAME': ':memory:'}}
