from backend.api_v3.models import Result
from backend.logger.models import HTTPRequest


def http_requests_without_results():
    all_results = Result.objects.all().values_list('request_sha1', flat=True)
    requests_without_results = HTTPRequest.objects.filter(api_version=3, data__isnull=False).exclude(
        sha1__in=list(all_results))
    return requests_without_results
