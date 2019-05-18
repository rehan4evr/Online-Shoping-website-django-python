"""
Django settings for socialauth project.

Generated by 'django-admin startproject' using Django 1.11.14.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
from django.urls import reverse_lazy

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '!r-2pbd5x+3tr%%2)ht138970=ixq)f3s5$ve*+%h+ea%v!t=x'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'social_django',
    'paypal.standard.ipn',
    'myapp',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',  # <--
]

ROOT_URLCONF = 'socialauth.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

AUTHENTICATION_BACKENDS=(   
    'social_core.backends.google.GoogleOAuth2',
    'social_core.backends.facebook.FacebookOAuth2',
    'django.contrib.auth.backends.ModelBackend',
    #   'social.backends.linkedin.LinkedinOAuth2',
    )

WSGI_APPLICATION = 'socialauth.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'shoppingdb',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST':'localhost',
        'PORT': '5432',
    },
}
AUTH_USER_MODEL = 'myapp.MyUser'


GOOGLE_RECAPTCHA_SECRET_KEY = '6LcXOqQUAAAAANCxJtfPEJivTPh7qdMa98Rb7cdO'

SOCIAL_AUTH_FACEBOOK_KEY ='310373552954331' 
SOCIAL_AUTH_FACEBOOK_SECRET = 'e72027919de8e7eb67c857170fe962df'


SOCIAL_AUTH_GOOGLE_OAUTH2_KEY ='1042944045422-6cda0u1dvvhp4eas5okqtr9h5vamr4j2.apps.googleusercontent.com' 
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'Ymx173_gm5aREuelOTVoTJiB'


SOCIAL_AUTH_LINKEDIN_OAUTH2_KEY = "81z5ythswm8t18"         #Client ID
SOCIAL_AUTH_LINKEDIN_OAUTH2_SECRET = "CTMcLUFxUjuZHA0P"  #Client Secret
SOCIAL_AUTH_LINKEDIN_OAUTH2_SCOPE = ['r_basicprofile', 'r_emailaddress']
SOCIAL_AUTH_LINKEDIN_OAUTH2_FIELD_SELECTORS = ['email-address', 'formatted-name', 'public-profile-url', 'picture-url']
SOCIAL_AUTH_LINKEDIN_OAUTH2_EXTRA_DATA = [
        ('id', 'id'),
        ('formattedName', 'name'),
        ('emailAddress', 'email_address'),
        ('pictureUrl', 'picture_url'),
        ('publicProfileUrl', 'profile_url'),
    ]


SOCIAL_AUTH_INSTAGRAM_KEY = "19fdf4886c814c97a801f59578a606d5"         #Client ID
SOCIAL_AUTH_INSTAGRAM_SECRET = "fb888dd44e6c4fac81f429f8a01cee6b"  #Client SECRET
SOCIAL_AUTH_INSTAGRAM_EXTRA_DATA = [         ('user', 'user'),
]


STRIPE_SECRET_KEY = 'sk_test_LZCjoEA966N6uwZDG7VzMGrL00fh5B8QYm'
STRIPE_PUBLISHABLE_KEY = 'pk_test_iRuB8ytUrcmckHzBKk7W7Xly00EELrr5ME'
GEOPOSITION_GOOGLE_MAPS_API_KEY = 'AIzaSyCm8rnRUZU0ecO8hpCF3KVANv9LmAXv0hc'
# SOCIAL_AUTH_FACEBOOK_KEY ='310373552954331' 
# SOCIAL_AUTH_FACEBOOK_SECRET = 'e72027919de8e7eb67c857170fe962df'


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

LOGIN_REDIRECT_URL=reverse_lazy('myapp:home')
LOGIN_URL=reverse_lazy('myapp:login')
LOGOUT_URL=reverse_lazy('myapp:logout')



STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]


MEDIA_ROOT=os.path.join(BASE_DIR,'media')
MEDIA_URL='/media/'

PAYPAL_RECEIVER_EMAIL="aftab4evr786-facilitator@gmail.com"
PAYPAL_TEST=False



