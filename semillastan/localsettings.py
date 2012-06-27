DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'stanleydb', # Or path to database file if using sqlite3.
        'USER': 'rodxavier', # Not used with sqlite3.
        'PASSWORD': 'rodxavierdbpassword1234567890', # Not used with sqlite3.
        'HOST': 'localhost', # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '', # Set to empty string for default. Not used with sqlite3.
    }
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'semillastan.db', # Or path to database file if using sqlite3.
        'USER': '', # Not used with sqlite3.
        'PASSWORD': '', # Not used with sqlite3.
        'HOST': '', # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '', # Set to empty string for default. Not used with sqlite3.
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'mail@semillastan.com'
EMAIL_HOST_PASSWORD = 'naitansemilla'
EMAIL_USE_TLS = True
SERVER_EMAIL = 'mail@semillastan.com'
SEND_BROKEN_LINK_EMAILS = 'True'

TWITTER_CONSUMER_KEY         = 'VivsfOZPyRsxiluO1zing'
TWITTER_CONSUMER_SECRET      = 'L5QN8u2a6e2zdNxhupMr1Q3mUUiTlF81HyNgkOdM4'
FACEBOOK_APP_ID              = '219643851429650'
FACEBOOK_API_SECRET          = '262af6fbf79e19fccff91539720f96c5'
FLICKR_API_KEY               = 'a8b28f96a743a79e9107ba81fea9f6bd'
FLICKR_API_SECRET            = '0d6d4e6dad7faf40'
