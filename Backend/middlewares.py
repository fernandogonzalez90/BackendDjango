from django.core.exceptions import DisallowedHost
import logging

from API.models import LogEntry

logger = logging.getLogger(__name__)


class BlockDisallowedHostMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            response = self.get_response(request)
        except DisallowedHost:
            LogEntry.objects.create(
                level='Warning',
                message=f'Disallowed host: {request.get_host()}',
                source='BlockDisallowedHostMiddleware'
            )
            logger.warning(f'Disable host:  {request.get_host()}')
            raise
        return response
