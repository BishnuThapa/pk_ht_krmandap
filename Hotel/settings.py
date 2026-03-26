
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/6.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-asp-rw)s3k*0))yg-n-9b27z-0&j$!=w8qd_m5=bu8&^^_!z29'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
     'django_daisy',
    'django.contrib.admin',
    'django.contrib.humanize',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django_ckeditor_5',

    'core',
    'aboutus',
    'attraction',
    'accounts',
    'blog',
    'facility',
    'faq',
    'inquiry',
    'offer',
    'ota',
    'page',
    'seo',
    'gallery',
    'popup',
    'slider',
    'settings',
    'services',
]

AUTH_USER_MODEL = 'accounts.Account'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Hotel.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'core.context_processor.default',
            ],
        },
    },
]

WSGI_APPLICATION = 'Hotel.wsgi.application'


# Database
# https://docs.djangoproject.com/en/6.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/6.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/6.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/6.0/howto/static-files/

# STATIC_ROOT = '/home3/etihadte/TulsiKathmanduHotel/staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOWS_CREDENTIALS = True


customColorPalette = [
    {
        'color': 'hsl(4, 90%, 58%)',
        'label': 'Red'
    },
    {
        'color': 'hsl(340, 82%, 52%)',
        'label': 'Pink'
    },
    {
        'color': 'hsl(291, 64%, 42%)',
        'label': 'Purple'
    },
    {
        'color': 'hsl(262, 52%, 47%)',
        'label': 'Deep Purple'
    },
    {
        'color': 'hsl(231, 48%, 48%)',
        'label': 'Indigo'
    },
    {
        'color': 'hsl(207, 90%, 54%)',
        'label': 'Blue'
    },
]

CKEDITOR_5_CUSTOM_CSS = 'path_to.css'  # optional
CKEDITOR_5_FILE_STORAGE = "path_to_storage.CustomStorage"  # optional
CKEDITOR_5_CONFIGS = {
    'default': {
        'toolbar': {
            'items': ['heading', '|', 'bold', 'italic', 'link',
                      'bulletedList', 'numberedList', 'blockQuote', 'imageUpload', ],
        }

    },
    'extends': {
        'blockToolbar': [
            'paragraph', 'heading1', 'heading2', 'heading3',
            '|',
            'bulletedList', 'numberedList',
            '|',
            'blockQuote',
        ],
        'toolbar': {
            'items': ['heading', '|', 'outdent', 'indent', '|', 'bold', 'italic', 'link', 'underline', 'strikethrough',
                      'code', 'subscript', 'superscript', 'highlight', '|', 'codeBlock', 'sourceEditing', 'insertImage',
                      'bulletedList', 'numberedList', 'todoList', '|',  'blockQuote', 'imageUpload', '|',
                      'fontSize', 'fontFamily', 'fontColor', 'fontBackgroundColor', 'mediaEmbed', 'removeFormat',
                      'insertTable',
                      ],
            'shouldNotGroupWhenFull': 'true'
        },
        'image': {
            'toolbar': ['imageTextAlternative', '|', 'imageStyle:alignLeft',
                        'imageStyle:alignRight', 'imageStyle:alignCenter', 'imageStyle:side',  '|'],
            'styles': [
                'full',
                'side',
                'alignLeft',
                'alignRight',
                'alignCenter',
            ]

        },
        'table': {
            'contentToolbar': ['tableColumn', 'tableRow', 'mergeTableCells',
                               'tableProperties', 'tableCellProperties'],
            'tableProperties': {
                'borderColors': customColorPalette,
                'backgroundColors': customColorPalette
            },
            'tableCellProperties': {
                'borderColors': customColorPalette,
                'backgroundColors': customColorPalette
            }
        },
        'heading': {
            'options': [
                {'model': 'paragraph', 'title': 'Paragraph',
                 'class': 'ck-heading_paragraph'},
                {'model': 'heading1', 'view': 'h1',
                 'title': 'Heading 1', 'class': 'ck-heading_heading1'},
                {'model': 'heading2', 'view': 'h2',
                 'title': 'Heading 2', 'class': 'ck-heading_heading2'},
                {'model': 'heading3', 'view': 'h3',
                 'title': 'Heading 3', 'class': 'ck-heading_heading3'}
            ]
        }
    },
    'list': {
        'properties': {
            'styles': 'true',
            'startIndex': 'true',
            'reversed': 'true',
        }
    }
}

# Define a constant in settings.py to specify file upload permissions
# Possible values: "staff", "authenticated", "any"
CKEDITOR_5_FILE_UPLOAD_PERMISSION = "staff"


# Django Daisy settings
DAISY_SETTINGS = {
    'SITE_TITLE': 'KR Mandap Admin',  # The title of the site
    # Header text displayed in the admin panel
    'SITE_HEADER': 'KR Mandap Hotel',
    # The title for the index page of dashboard
    'INDEX_TITLE': 'Hi, welcome to your dashboard',
    # Path to the logo image displayed in the sidebar
    # 'SITE_LOGO': '/static/admin/img/daisyui-logomark.svg',
    # List of extra stylesheets to be loaded in base.html (optional)
    'EXTRA_STYLES': [],
    # List of extra script URLs to be loaded in base.html (optional)
    'EXTRA_SCRIPTS': [],
    # If True, loads full DaisyUI components in the admin (useful if you have custom template overrides)
    'LOAD_FULL_STYLES': False,
    # If True, the filter sidebar will open by default on changelist views
    'SHOW_CHANGELIST_FILTER': False,
    'DONT_SUPPORT_ME': False,  # Hide github link in sidebar footer
    'SIDEBAR_FOOTNOTE': '',  # add footnote to sidebar
    'APPS_REORDER': {
        # Custom configurations for third-party apps that can't be modified directly in their `apps.py`
        'auth': {
            # FontAwesome icon for the 'auth' app
            'icon': 'fa-solid fa-person-military-pointing',
            'name': 'Authentication',  # Custom name for the 'auth' app
            # Whether to hide the 'auth' app from the sidebar (set to True to hide)
            'hide': False,
            'divider_title': "Auth",  # Divider title for the 'auth' section
        },
        'social_django': {
            # Custom FontAwesome icon for the 'social_django' app
            'icon': 'fa-solid fa-users-gear',
        },
    },
}
