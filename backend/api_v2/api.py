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


class APIv2(View):
    http_method_names = ['get', 'post', 'options']

    def options(self, request, *args, **kwargs):
        response = HttpResponse(status=200)
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Methods'] = ', '.join(self.http_method_names).upper()
        response['Access-Control-Allow-Headers'] = 'Content-Type'
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
        response = JsonResponse(data={})
        response['Access-Control-Allow-Origin'] = '*'

        http_request_sha1, created = HTTPRequest.add(request, api_version=2)

        if not created:
            response['status'] = 200
            response['data'] = {'message': 'Response already uploaded', 'sha1': http_request_sha1.sha1}
            return response

        try:
            data = json.loads(request.body, object_hook=json_decode)
            Trial.add(
                http_request_sha1=http_request_sha1,
                trial=data.get('trial', None),
                surveys=data.get('survey', None),
                clicks=data.get('clicks', None),
                events=data.get('events', None),
            )
            response['status'] = 201
            response['data'] = {'message': 'Trial added to the database.', 'sha1': http_request_sha1.sha1}
            return response

        except IntegrityError:
            response['status'] = 200
            response['data'] = {'message': 'Response already uploaded', 'sha1': http_request_sha1.sha1}
            return response

        except (json.decoder.JSONDecodeError, ValidationError, ValueError, TypeError):
            response['status'] = 400
            response['data'] = {'message': 'Bad Request'}
            return response
