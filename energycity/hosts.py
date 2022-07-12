from django.conf import settings
from django_hosts import patterns, host



host_patterns = patterns(
    '',
    host(r'www', 'energycity.frontend_urls', name='www'),
    host(r'admin', settings.ROOT_URLCONF, name='admin'),
    host(r'api', 'energycity.api_urls', name='api'),
)