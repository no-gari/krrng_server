from .base import *
import pymysql
import os
from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage
pymysql.install_as_MySQLdb()

DEBUG = True

CORS_ALLOW_ALL_ORIGINS = True

ALLOWED_HOSTS = ['*', '127.0.0.1']

DB = 'mysql'

if DB == 'sqlite':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
if DB == 'mysql':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'krrngrds',
            'USER': 'krrngrds',
            'PASSWORD': 'krrngrds',
            'HOST': 'krrngrds.ci0gyj4wz5ig.ap-northeast-2.rds.amazonaws.com',
            'PORT': '3306',
            'OPTIONS': {
                'charset': 'utf8mb4',
                'use_unicode': True,
            }
        }
    }

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

AWS_STORAGE_BUCKET_NAME = "krrng"
AWS_S3_BUCKET_NAME_STATIC = "krrng"

AWS_LOCATION = 'static'
AWS_REGION = 'ap-northeast-2'
AWS_QUERYSTRING_AUTH = False
AWS_S3_HOST = 's3.%s.amazonaws.com' % AWS_REGION
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
STATIC_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/static/"

# AWS_ACCESS_KEY_ID = 'AKIATHT2BVX2LCU2YP6U'
# AWS_SECRET_ACCESS_KEY = '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'

AWS_DEFAULT_ACL = "public-read-write"
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}
