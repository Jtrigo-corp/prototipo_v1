"""
Django settings for proyectopersonal project.
Configuracion Django para Prototipo_web_V1
"""
 
import os
 
# Constructor de rutas dentro del proyecto 
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
 
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '4f8h3=9z@^kui2#+fnr^@rs(4ihz-)@kun==s7b$-!&pli$3j9'
 
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
 
ALLOWED_HOSTS = []
 
# Definicion de la aplicacion
 
apps_instaladas = [
    'app1.apps.App1Config',
    'rest_framework',
    'rest_framework.authtoken',
    'bootstrap3',
    'django.contrib.sites',
    'rest_auth',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'rest_auth.registration',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
 
midleware= [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
 
 
ACCESS_KEY = 'AKIASDFDSGGFDGW7CNJA'                       #AWS Access Key ID
PASS_KEY = 'L77973V7+E3q2ZYasdasdsa98989702ayK0ZUE'  #AWS Secret Access Key
 
ROOT_URLCONF = 'Prototipo_web_V1.urls'
 
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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
 
WSGI_APPLICATION = 'Prototipo_SGI'
 
 
# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
 
DATABASE = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
 
 
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
 
LANGUAGE_CODE = 'es-es'
 
TIME_ZONE = 'UTC'
 
USE_I18N = True
 
USE_L10N = True
 
USE_TZ = True
 
 
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/
 
STATIC_URL = '/static/'
 
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static")
]
 
 
# Default settings
BOOTSTRAP3 = {
 
    # URL JQUERY
    'jquery_url': '//code.jquery.com/jquery.min.js',
    # URL Bootstrap
    'base_url': '//maxcdn.bootstrapcdn.com/bootstrap/3.3.7/',
    # URL CSS
    'css_url': None,
    # URL CSS temas
    'theme_url': None,
    # URL JavaScript 
    'javascript_url': None,
    # HEAD
    'javascript_in_head': False,
    # JQUERY CON BOOTSTRAP
    'include_jquery': False,
    # LABEL HORIZONTAL
    'horizontal_label_class': 'col-md-3',
    # formulario horizontal
    'horizontal_field_class': 'col-md-9',
    # atributos requeridos
    'set_required': True,
    # atributos desactivados
    'set_disabled': False,
    # atributos de placeholder
    'set_placeholder': True,
    # clase requerida de css
    'required_css_class': '',
    # clase que indica error
    'error_css_class': 'has-error',
    # clase que indica valides
    'success_css_class': 'has-success',
    # renderizador
    'formset_renderers':{
        'default': 'bootstrap3.renderers.FormsetRenderer',
    },
    'form_renderers': {
        'default': 'bootstrap3.renderers.FormRenderer',
    },
    'field_renderers': {
        'default': 'bootstrap3.renderers.FieldRenderer',
        'inline': 'bootstrap3.renderers.InlineFieldRenderer',
    },
}
SITE_ID = 1