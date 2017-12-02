import datetime
import json

from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError
from django.http import HttpResponse
from django.http import JsonResponse
from django.utils.datastructures import MultiValueDictKeyError
from django.views.generic import View

from backend._common.utils import json_datetime_decoder
from backend.logger.models import HTTPRequest
from backend.api_v3.models import Result


class APIv3(View):
    http_method_names = ['get', 'post', 'options']

    def options(self, request, *args, **kwargs):
        response = HttpResponse(status=200)
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Methods'] = ', '.join(self.http_method_names).upper()
        response['Access-Control-Allow-Headers'] = 'Content-Type'
        return response

    def get(self, request, *args, **kwargs):
        response = JsonResponse(data={})
        response['Access-Control-Allow-Origin'] = '*'
        response['Cache-Control'] = 'no-cache, no-store, must-revalidate'

        try:
            start_datetime = datetime.datetime.strptime(request.GET['start_datetime'], '%Y-%m-%dT%H:%M:%S.%fZ').replace(tzinfo=datetime.timezone.utc)
            result = Result.objects.filter(start_datetime=start_datetime)[0]
            return JsonResponse(status=200, data=result.get_data())

        except (Result.DoesNotExist, IndexError):
            response['status'] = 404
            response['data'] = {'code': 404, 'status': 'Not Found', 'message': 'Result Does Not Exists'}
        except MultiValueDictKeyError:
            response['status'] = 400
            response['data'] = {'code': 400, 'status': 'Bad Request', 'message': 'Bad Request'}

        return response

    def post(self, request, *args, **kwargs):
        response = JsonResponse(data={})
        response['Access-Control-Allow-Origin'] = '*'
        response['Cache-Control'] = 'no-cache, no-store, must-revalidate'

        http_request, created = HTTPRequest.add(request, api_version=3)

        if not created:
            response['status'] = 200
            response['data'] = {'message': 'Response already uploaded', 'sha1': http_request.sha1}
            return response

        try:
            data = json.loads(str(request.body, encoding='utf-8'), object_hook=json_datetime_decoder)
            Result.add(
                request_sha1=http_request.sha1,
                clicks=data.pop('clicks'),
                result=data,
            )

            response['status'] = 201
            response['data'] = {'message': 'Result added to the database.', 'sha1': http_request.sha1}
            return response

        except IntegrityError:
            http_request.valid()
            response['status'] = 200
            response['data'] = {'message': 'Response already uploaded', 'sha1': http_request.sha1}
            return response

        except Exception as message:
            response['status'] = 400
            response['data'] = {'message': 'Bad Request'}
            http_request.error(message)
            return response
