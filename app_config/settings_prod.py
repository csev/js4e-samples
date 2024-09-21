
# Alter the settings for a production deployment. Activate this
# Configuration locally using
#
# python manage.py runserver --settings=app_config.settings_prod
#
# On PythonAnywhere put this into the WGSI Configuration on the Web tab
#
'''
import os
import sys

path = os.path.expanduser('~/django_projects/mysite')
if path not in sys.path:
    sys.path.insert(0, path)
os.environ['DJANGO_SETTINGS_MODULE'] = 'app_config.settings_prod'
from django.core.wsgi import get_wsgi_application
from django.contrib.staticfiles.handlers import StaticFilesHandler
application = StaticFilesHandler(get_wsgi_application())
'''

from .settings import *

print('Running app_config.settings_prod from', __file__);

# Before using a MySQL database, make sure to 
# 
# pip install mysqlclient

# Connect to a MySQL database on PythonAnywhere instead of 

PYAW_DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'drchuck$chucklist',
        'USER': 'js4e',
        'PASSWORD': '3209udji843',
        'HOST': 'js4e.mysql.pythonanywhere-services.com',
         'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}

# To create a database on a local MySQL server
# CREATE DATABASE js4e_database DEFAULT CHARACTER SET UTF8;

# CREATE USER IF NOT EXISTS 'js4e_user'@'127.0.0.1' IDENTIFIED BY 'sakaiger';
# ALTER USER 'js4e_user'@'127.0.0.1' IDENTIFIED BY 'sakaiger';

# GRANT ALL ON js4e_database.* TO 'js4e_user'@'127.0.0.1';

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'js4e_database',
        'USER': 'js4e_user',
        'PASSWORD': 'sakaiger',
        'HOST': '127.0.0.1',
        'PORT': '8889',
         'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}

