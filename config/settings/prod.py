DEBUG = False

ALLOWED_HOSTS = ['api.domain.com', 'admin.domain.com']

CORS_ALLOWED_ORIGINS = [
    'https://frontend-domain.com',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres123!',
        'HOST': 'postgres',
        'PORT': '5432',
    }
}

# S3
AWS_ACCESS_KEY_ID = '**'
AWS_SECRET_ACCESS_KEY = '**'
AWS_REGION = 'ap-northeast-2'
AWS_STORAGE_BUCKET_NAME = 'singoro-mediafiles'
AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.{AWS_REGION}.amazonaws.com'
AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=864000'}
AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = 'public-read'
AWS_LOCATION = 'media'
AWS_S3_SECURE_URLS = True
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
MEDIAFILES_LOCATION = 'media'

