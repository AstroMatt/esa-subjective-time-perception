import datetime
import json

from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.generic import View

from backend._common.utils import json_datetime_decoder
from backend.logger.models import HTTPRequest
from backend.api_v3.models import Result


class APIv3View(View):
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
            result = Result.objects.get(start_datetime=start_datetime)
            response = JsonResponse(status=200, data={'code': 200, 'status': 'OK', 'data': result.get_data()})

        except (Result.DoesNotExist, IndexError):
            response = JsonResponse(status=400, data={'code': 404, 'status': 'Not Found', 'message': 'Result Does Not Exists'})

        response['Access-Control-Allow-Origin'] = '*'
        return response

    def post(self, request, *args, **kwargs):
        response = JsonResponse(data={})
        response['Access-Control-Allow-Origin'] = '*'

        http_request_sha1, created = HTTPRequest.add(request, api_version=3)

        if not created:
            response['status'] = 200
            response['data'] = {'message': 'Response already uploaded', 'sha1': http_request_sha1.sha1}
            return response

        try:
            data = json.loads(str(request.body, encoding='utf-8'), object_hook=json_datetime_decoder)
            Result.add(
                http_request_sha1=http_request_sha1.sha1,
                clicks=data.pop('clicks'),
                result=data,
            )
            response['status'] = 201
            response['data'] = {'message': 'Result added to the database.', 'sha1': http_request_sha1.sha1}
            return response

        except IntegrityError:
            response['status'] = 200
            response['data'] = {'message': 'Response already uploaded', 'sha1': http_request_sha1.sha1}
            return response

        except (json.decoder.JSONDecodeError, ValidationError, ValueError, TypeError):
            response['status'] = 400
            response['data'] = {'message': 'Bad Request'}
            return response
