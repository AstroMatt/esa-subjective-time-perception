import json
from django.core.management.base import BaseCommand
from backend.api_v3.models import Result
from backend.logger.models import HTTPRequest
from backend._common.utils import json_datetime_decoder


class Command(BaseCommand):
    help = 'Check which HTTP requests were not parsed as Results'

    def handle(self, *args, **options):
        all_results = Result.objects.all().values_list('request_sha1', flat=True)

        requests_without_results = HTTPRequest.objects \
            .filter(api_version=3, data__isnull=False) \
            .exclude(sha1__in=list(all_results))

        integrity_errors = HTTPRequest.objects.filter(integrity=HTTPRequest.INTEGRITY_ERROR)

        for request in requests_without_results | integrity_errors:
            print(request)
            data = json.loads(request.data, object_hook=json_datetime_decoder)
            Result.add(
                request_sha1=request.sha1,
                clicks=data.pop('clicks'),
                result=data,
            )
