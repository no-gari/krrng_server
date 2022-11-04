import datetime
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'pj%2ze09(g)i^joilp-f8gvs)6ou_m036u3ejs^ky&9nse5k92'

# SECURITY WARNING: don't run with debug turned on in production!


# Application definition
DJANGO_APPS = [
    'admin_volt.apps.AdminVoltConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

LOCAL_APPS = [
    'api.user.apps.UserConfig',
    'api.logger.apps.LoggerConfig',
    'api.animal.apps.AnimalConfig',
    'api.hospital.apps.HospitalConfig',
    'api.commerce.apps.CommerceConfig',
    'api.customerservice.apps.CustomerserviceConfig',
]

# COMMERCE API APPS
COMMERCE_APPS = [
    'api.commerce.cart.apps.CartConfig',
    'api.commerce.brand.apps.BrandConfig',
    'api.commerce.order.apps.OrderConfig',
    'api.commerce.review.apps.ReviewConfig',
    'api.commerce.search.apps.SearchConfig',
    'api.commerce.coupon.apps.CouponConfig',
    'api.commerce.comment.apps.CommentConfig',
    'api.commerce.product.apps.ProductConfig',
    'api.commerce.customer.apps.CustomerConfig',
    'api.commerce.collection.apps.CollectionConfig',
]

THIRD_PARTY_APPS = [
    'rest_framework',
    'corsheaders',
    'django_crontab',
    'django_filters',
    'django_hosts',
    'drf_yasg',
    'storages',
]

INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS + COMMERCE_APPS + THIRD_PARTY_APPS


MIDDLEWARE = [
    'django_hosts.middleware.HostsRequestMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates')
        ],
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


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'ko'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

SITE_NAME = 'banhae'

# STATIC_URL = '/static/'
# STATIC_ROOT = BASE_DIR / 'static'
#
# MEDIA_URL = '/media/'
# MEDIA_ROOT = BASE_DIR / 'media'

# DJANGO BASE USER MODEL
SITE_ID = 1

# AUTH_USER_MODEL
AUTH_USER_MODEL = 'user.User'

# APPLICATION
WSGI_APPLICATION = 'config.wsgi.application'
ASGI_APPLICATION = 'config.routing.application'


# HOST
DEFAULT_HOST = 'api'
ROOT_HOSTCONF = 'config.hosts'
ROOT_URLCONF = 'config.urls.api'


# JWT
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': datetime.timedelta(weeks=9999),
    'REFRESH_TOKEN_LIFETIME': datetime.timedelta(weeks=9999),
    'ROTATE_REFRESH_TOKENS': True,
}


# DJANGO REST FRAMEWORK
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_RENDERER_CLASSES': [
        'djangorestframework_camel_case.render.CamelCaseJSONRenderer',
        'djangorestframework_camel_case.render.CamelCaseBrowsableAPIRenderer',
    ],
    'DEFAULT_PARSER_CLASSES': [
        'djangorestframework_camel_case.parser.CamelCaseFormParser',
        'djangorestframework_camel_case.parser.CamelCaseMultiPartParser',
        'djangorestframework_camel_case.parser.CamelCaseJSONParser',
    ],
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
    ],
}


# SWAGGER
SWAGGER_SETTINGS = {
    'DEFAULT_AUTO_SCHEMA_CLASS': 'config.swagger.SquadSwaggerAutoSchema',
    'USE_SESSION_AUTH': True,
    'DOC_EXPANSION': 'list',
    'APIS_SORTER': 'alpha',
    'SECURITY_DEFINITIONS': None,
    'DEFAULT_API_URL': 'http://127.0.0.1:8000/api/'
}

# COOLSMS
COOLSMS_API_KEY = 'NCSPWDDE4TYZVTQU'
COOLSMS_API_SECRET = '9ZEGRBLTMMIKMPDTUPNZUVYGIICO3WEF'
COOLSMS_FROM_PHONE = '01099051104'


# CLAYFUL
CLAYFUL_API_KEY = '2118f16ce0138ef9d9093461d40bb3d2d016ec73a4d73de2c26471feb9d797e0e87b50f2'
CLAYFUL_API_SECRET = 'b827a0018b9e4cf048127ef5b5e84d10978dc9e41ec515d563d35382d67baa3c89d8f2b4a2d33cb2b8ae407c15c35451'
CLAYFUL_BACKEND_TOKEN = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6IjdlN2QxMmRjMGM0MGM4NzFhZTEyZjFjZmIzYTNkZTMxMDc5NzM1YmY4OGMyMzZiOWI2ZTY2MzkxZjhlYzc5OTUiLCJyb2xlIjoiY2xpZW50IiwiaWF0IjoxNjY0Nzg2MDgwLCJzdG9yZSI6IkdLNEFCM1hIVzk4My5SN1hYN0NIWlM4S1MiLCJzdWIiOiJHRFpBVU1HQ0xYU1cifQ.k4Js5BYO-1GWfgruqxWkPEMN0j00HFIGXeH7KKYMpMo'
CLAYFUL_PRODUCTS_ID = 'SJGJJ72PK5TW'
CLAYFUL_COLLECTION_ID = 'BR9KT8ZJPSFK'
CLAYFUL_BANNER_ID = 'DAZCMCFDX2Z2'
CLAYFUL_SHIPPING_ID = 'BJEYDMZKZ8RJ'
CLAYFUL_COUPON_ID = 'QF32EJB45DH9'
CLAYFUL_PAYMENT_METHOD = '5F5G4WCZMAVS'

# IAMPORT
IAMPORT_CODE = 'imp30008433'
IAMPORT_KEY = '0330942419168537'
IAMPORT_SECRET = 'iogg8L0d5kh3MwuXrDAi9V3uZ7uNzP9Seq8nc8AhtSlfpQdRtO9DJc7IkBwUrFMF6V2i3DAwvVMUM0Lf'
IMPORT_EXPORT_USE_TRANSACTIONS = True
