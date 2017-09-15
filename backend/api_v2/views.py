import datetime
import json
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.generic import View
from backend.api_v2.models import Trial
from backend.logger.models import HTTPRequest
from backend.api_v2.utils import json_decode


class APIv2View(View):
    http_method_names = ['get', 'post', 'head']

    def head(self, request, *args, **kwargs):
        response = HttpResponse(status=200)
        response['Access-Control-Allow-Origin'] = '*'
        return response

    def get(self, request, *args, **kwargs):
        try:
            start_datetime = datetime.datetime.strptime(request.GET['start_datetime'], '%Y-%m-%dT%H:%M:%S.%fZ')
            trial = Trial.objects.get(start_datetime=start_datetime)
            response = JsonResponse(status=200, data={'code': 200, 'status': 'OK', 'data': trial.get_data()})

        except (Trial.DoesNotExist, IndexError):
            response = JsonResponse(status=400, data={'code': 404, 'status': 'Not Found', 'message': 'Trial Does Not Exists'})

        response['Access-Control-Allow-Origin'] = '*'
        return response

    def post(self, request, *args, **kwargs):
        try:
            http_request_sha1 = HTTPRequest.add(request, api_version=2)
            data = json.loads(request.body, object_hook=json_decode)
            Trial.add(
                http_request_sha1=http_request_sha1,
                trial=data.get('trial', None),
                surveys=data.get('survey', None),
                clicks=data.get('clicks', None),
                events=data.get('events', None),
            )
            response = JsonResponse(status=201, data={'code': 201, 'status': 'Created', 'message': 'Trial added to the database.', 'sha1': http_request_sha1})

        except (json.decoder.JSONDecodeError, IntegrityError, ValidationError, ValueError):
            response = JsonResponse(status=400, data={'code': 400, 'status': 'Bad Request', 'message': 'JSON decode error'})

        response['Access-Control-Allow-Origin'] = '*'
        return response
