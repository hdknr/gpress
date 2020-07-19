import os

SETTINGS_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(SETTINGS_DIR)


WORDPRESS = {
    'ENGINE': 'django.db.backends.mysql',
    'HOST': 'localhost',
    'NAME': 'wpdb',
    'USER': 'wpuser',
    'PASSWORD': 'wppass',
}
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
    'wordpress': WORDPRESS,
}
ALLOWED_HOSTS = ['www.foo.com', ]

