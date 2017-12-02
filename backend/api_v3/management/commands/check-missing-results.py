import json
from django.core.management.base import BaseCommand
from backend.api_v3.models import Result
from backend.logger.models import HTTPRequest


class Command(BaseCommand):
    help = 'Check which HTTP requests were not parsed as Results'

    def handle(self, *args, **options):
        print(f'\n\nResults which do not have "HTTP Requests":')

        all_requests = HTTPRequest.objects.filter(api_version=3).values_list('sha1', flat=True)
        results_without_requests = Result.objects.all().exclude(request_sha1__in=list(all_requests))

        for result_without_request in results_without_requests:
            print(result_without_request)

        print(f'\n\nRequests which do not have calculated results:')

        all_results = Result.objects.all().values_list('request_sha1', flat=True)
        requests_without_results = HTTPRequest.objects.filter(api_version=3, data__isnull=False).exclude(sha1__in=list(all_results))

        for missing_result in requests_without_results:
            try:
                email = json.loads(missing_result.data).get('email', '/* no email set in survey */')
                print(missing_result, email)
            except AttributeError:
                print(missing_result)

        print(f'\n\nproblems: {len(requests_without_results)}')
