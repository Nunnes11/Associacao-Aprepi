from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-3@g)$r-6f6jt7$ug)xp@y(!^5*1r1zjxlcou8#)$cwq4u(d78g'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']


# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'aprepi',
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

ROOT_URLCONF = 'Associacao.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Associacao.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'aprepi',
        'USER': 'root',
        'PASSWORD': 'Admin123!',
        'HOST': 'localhost',
        'PORT': 3306
    }
}

# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Fortaleza'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

LOGIN_URL = '/login/'

# Customização do 'Admin do Django' usando JAZZMIN
JAZZMIN_SETTINGS = {
"site_title": "Aprepi",
"site_header": "Painel Administrativo",
"site_brand": "Aprepi",
"welcome_sign": "Bem-vindo ao painel administrativo!",
"copyright": "Aprepi © 2025",

# Logo e ícone (coloque os arquivos em static/images)
"site_logo": "logo/logo.png",
"site_logo_classes": "img-circle",
"site_icon": "images/favicon.ico",

# Ícones para apps e modelos
"icons": {
"auth": "fas fa-users-cog",
"auth.User": "fas fa-user",
"auth.Group": "fas fa-users",
# exemplo para um app "noticias"
"noticias.Noticia": "fas fa-newspaper",
},

# Ordem e agrupamento de apps
"order_with_respect_to": ["auth", "noticias"],

"custom_css": "css/custom_admin.css",

# Mostrar ou não o builder de UI
"show_ui_builder": True,
}

JAZZMIN_UI_TWEAKS = {
    "theme": "flatly",  # tema claro
    "navbar": "navbar-primary",
    "sidebar": "sidebar-primary",
    "footer_fixed": True,
    "navbar_fixed": True,
    "sidebar_fixed": True,
}




