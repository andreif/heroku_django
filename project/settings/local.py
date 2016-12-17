from .base import *

assert not DEBUG, "base settings must set DEBUG to False"
DEBUG = True
ALLOWED_HOSTS = ['*']

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.PyLibMCCache',
        'LOCATION': '127.0.0.1:11211',
        'USERNAME': None,
        'PASSWORD': None,
        'BINARY': True,  # needed for authentication
        'TIMEOUT': None,  # disables expiration
        'OPTIONS': {
            'tcp_nodelay': True,  # Enable faster IO
            'tcp_keepalive': True,  # Keep connection alive

            # Timeout settings
            'connect_timeout': 2000,  # ms
            'send_timeout': 750 * 1000,  # us
            'receive_timeout': 750 * 1000,  # us
            '_poll_timeout': 2000,  # ms

            # Better failover
            'ketama': True,
            'remove_failed': 1,
            'retry_timeout': 2,
            'dead_timeout': 30,
        },
    }
}
