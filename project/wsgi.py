import os
from django.core.wsgi import get_wsgi_application
from dj_static import Cling

# Fix django closing connection to MemCachier after every request (#11331)
from django.core.cache.backends.memcached import BaseMemcachedCache
BaseMemcachedCache.close = lambda self, **kwargs: None

assert os.environ['DJANGO_SETTINGS_MODULE']

application = Cling(get_wsgi_application())
