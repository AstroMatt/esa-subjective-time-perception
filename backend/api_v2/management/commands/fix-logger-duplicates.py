from django.core.management.base import BaseCommand
from backend.logger.models import RequestLogger
from backend.logger.models import HTTPRequest


class Command(BaseCommand):
    help = 'Request Logger remove duplicates'

    def handle(self, *args, **options):
        for request in RequestLogger.objects.all():
            HTTPRequest.objects.get_or_create(
                sha1=request.sha1,
                defaults={
                    'datetime': request.datetime,
                    'modified': request.modified,
                    'ip': request.ip,
                    'api_version': request.api_version,
                    'method': request.method,
                    'data': request.data
                }
            )