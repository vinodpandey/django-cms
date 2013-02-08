from settings.default import *
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': SECRETS['database_name'],                      # Or path to database file if using sqlite3.
        'USER': SECRETS['database_user'],                      # Not used with sqlite3.
        'PASSWORD': SECRETS['database_passwd'],                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}
