from mysite.settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'doc_search_test',
        'HOST': 'localhost',
    }
}
