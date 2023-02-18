"""
Django settings for conf project.

Generated by 'django-admin startproject' using Django 3.2.16.

For more information on this file, see©
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from django.test.signals import setting_changed
from django.conf import settings as django_settings
import datetime
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-8j8k)&0lt3&mg79-=1vdw%y5r_v(^w=qpr^bnl!lm=vl2_1lgg'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


APPEND_SLASH = True


GRAPHQL_JWT = {
    "JWT_VERIFY_EXPIRATION": True,
    "JWT_AUTH_HEADER_PREFIX": "Bearer",
    "JWT_LONG_RUNNING_REFRESH_TOKEN": True,
    "JWT_EXPIRATION_DELTA": datetime.timedelta(hours=9),
    "JWT_REFRESH_EXPIRATION_DELTA": datetime.timedelta(hours=9),
    "JWT_ALLOW_ANY_CLASSES": [
        # "secure_auth.mutations.Register",
        # "secure_auth.mutations.VerifyAccount",
        # "secure_auth.mutations.ResendActivationEmail",
        # "secure_auth.mutations.SendPasswordResetEmail",
        # "secure_auth.mutations.PasswordReset",
        # "secure_auth.mutations.ObtainJSONWebToken",
        # "secure_auth.mutations.VerifyToken",
        # "secure_auth.mutations.RefreshToken",
        # "secure_auth.mutations.RevokeToken",
        # "secure_auth.mutations.VerifySecondaryEmail",
        # "secure_auth.mutations.SlackAuthCode",
        # "secure_auth.mutations.VerifySecondaryEmail",
        # "graphql_social_auth.relay.SocialAuthJWT",
    ],
}


# import django.contrib.auth.backends

# Auth Backends
AUTHENTICATION_BACKENDS = [
    # "graphql_jwt.backends.JSONWebTokenBackend",
    "apps.auth.backends.GraphQLAuthBackend",
    "django.contrib.auth.backends.ModelBackend"
]


# Application definition

INSTALLED_APPS = [
    # 'daphne',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'graphene_django',
    'django_filters',
    'apps.account',
    'apps.auth',
    'apps.channel',
    'apps.checkout',
    'apps.core',
    'apps.customer',
    'apps.discount',
    'apps.giftcard',
    'apps.inventory',
    'apps.invoice',
    'apps.order',
    'apps.payment',
    'apps.permission',
    'apps.product',
    'apps.shipping',
    'apps.store',
    'apps.tax',

    # third party
    "graphql_jwt.refresh_token.apps.RefreshTokenConfig",


]

# from django.contrib.auth.middleware import AuthenticationMiddleware

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'conf.urls'

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

WSGI_APPLICATION = 'conf.wsgi.application'
ASGI_APPLICATION = "conf.asgi.application"


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Grphene settings
GRAPHENE = {
    "SCHEMA": "apps.core.schema.schema",
    "SCHEMA_OUTPUT": "schema.json",
    "SCHEMA_INDENT": 2,
    "MIDDLEWARE": [
        # "graphene_django.debug.DjangoDebugMiddleware",
        "graphql_jwt.middleware.JSONWebTokenMiddleware",
    ],
}

DEFAULT_AUTO_FIELD = "django.db.models.AutoField"


CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels.layers.InMemoryChannelLayer"
    }
}


AUTH_USER_MODEL = 'apps_auth.SEUser'


# CHANNEL_LAYERS = {
#     "default": {
#         "BACKEND": "channels_redis.core.RedisChannelLayer",
#         "CONFIG": {
#             "hosts": [("127.0.0.1", 6379)],
#         },
#     },
# }


# Email settings
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


DEFAULTS = {

    # email stuff
    "EMAIL_FROM": getattr(django_settings, "DEFAULT_FROM_EMAIL", "test@email.com"),
    "SEND_ACTIVATION_EMAIL": True,
    # client: example.com/activate/token
    "ACTIVATION_PATH_ON_EMAIL": "activate",
    "ACTIVATION_SECONDARY_EMAIL_PATH_ON_EMAIL": "activate",
    # client: example.com/password-set/token
    "PASSWORD_SET_PATH_ON_EMAIL": "password-set",
    # client: example.com/password-reset/token
    "PASSWORD_RESET_PATH_ON_EMAIL": "password-reset",
    # email subjects templates
    "EMAIL_SUBJECT_ACTIVATION": "email/activation_subject.txt",
    "EMAIL_SUBJECT_ACTIVATION_RESEND": "email/activation_subject.txt",
    "EMAIL_SUBJECT_SECONDARY_EMAIL_ACTIVATION": "email/activation_subject.txt",
    "EMAIL_SUBJECT_PASSWORD_SET": "email/password_set_subject.txt",
    "EMAIL_SUBJECT_PASSWORD_RESET": "email/password_reset_subject.txt",
    # email templates
    "EMAIL_TEMPLATE_ACTIVATION": "email/activation_email.html",
    "EMAIL_TEMPLATE_ACTIVATION_RESEND": "email/activation_email.html",
    "EMAIL_TEMPLATE_SECONDARY_EMAIL_ACTIVATION": "email/activation_email.html",
    "EMAIL_TEMPLATE_PASSWORD_SET": "email/password_set_email.html",
    "EMAIL_TEMPLATE_PASSWORD_RESET": "email/password_reset_email.html",
    "EMAIL_TEMPLATE_VARIABLES": {},
}


class GraphQLAuthSettings(object):
    """
    A settings object, that allows API settings to be accessed as properties.
    """

    def __init__(self, user_settings=None, defaults=None):
        if user_settings:
            self._user_settings = user_settings
        self.defaults = defaults or DEFAULTS

    @property
    def user_settings(self):
        if not hasattr(self, "_user_settings"):
            self._user_settings = getattr(django_settings, "GRAPHQL_AUTH", {})
        return self._user_settings

    def __getattr__(self, attr):
        if attr not in self.defaults:
            raise AttributeError(f"Invalid graphql_auth setting: '{attr}'")
        try:
            # Check if present in user settings
            val = self.user_settings[attr]
        except KeyError:
            # Fall back to defaults
            val = self.defaults[attr]

        # Cache the result
        setattr(self, attr, val)
        return val


graphql_auth_settings = GraphQLAuthSettings(None, DEFAULTS)


def reload_graphql_auth_settings(*args, **kwargs):
    global graphql_auth_settings
    setting, value = kwargs["setting"], kwargs["value"]
    if setting == "GRAPHQL_AUTH":
        graphql_auth_settings = GraphQLAuthSettings(value, DEFAULTS)


setting_changed.connect(reload_graphql_auth_settings)