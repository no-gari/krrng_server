from .base import *
import pymysql
import os

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
        }
    }

# S3
# USE_S3 = True
#
# if USE_S3:
#     DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
#     MEDIAFILES_LOCATION = 'media'
#
# AWS_S3_SECURE_URLS = True
# AWS_REGION = 'ap-northeast-2'
# AWS_STORAGE_BUCKET_NAME = 'krrng'
# AWS_QUERYSTRING_AUTH = False
# AWS_S3_HOST = 's3.%s.amazonaws.com' % AWS_REGION
# AWS_ACCESS_KEY_ID = 'AKIATHT2BVX2LCU2YP6U'
# AWS_SECRET_ACCESS_KEY = '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'
# AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
# AWS_DEFAULT_ACL = None
# AWS_S3_OBJECT_PARAMETERS = {
#     'CacheControl': 'max-age=86400',
# }

STATIC_URL = '/dev/static/'       # Use the name of your staging environment (e.g. production)
WHITENOISE_STATIC_PREFIX = '/static/'

YOUR_S3_BUCKET = "krrng"

STATICFILES_STORAGE = "django_s3_storage.storage.StaticS3Storage"
AWS_S3_BUCKET_NAME_STATIC = "krrng"

AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % YOUR_S3_BUCKET

AWS_ACCESS_KEY_ID = 'AKIATHT2BVX2LCU2YP6U'
AWS_SECRET_ACCESS_KEY = 'LxGZo9S1JpSNd8CiRO0FsHFVS5X8r5dc8Hh5+N1J'