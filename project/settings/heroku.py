from .base import *

assert not DEBUG, "base settings must set DEBUG to False"
ALLOWED_HOSTS = ['project']

DATABASES = {'default': dj_database_url.config()}

CACHES = {
    'default': {
        'BACKEND': 'project.cache.MemCachier',
        'LOCATION': os.environ['MEMCACHIER_SERVERS'].replace(',', ';'),
        'USERNAME': os.environ['MEMCACHIER_USERNAME'],
        'PASSWORD': os.environ['MEMCACHIER_PASSWORD'],
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
