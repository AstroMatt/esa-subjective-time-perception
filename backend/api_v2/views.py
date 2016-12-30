import datetime
import json
import logging
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.generic import View
from backend.api_v2.models import Trial

log = logging.getLogger('backend')


def datetime_decoder(obj):
    for key, value in obj.items():
        if key in ['datetime', 'start', 'end']:
           obj[key] = datetime.datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%fZ').replace(tzinfo=datetime.timezone.utc)
    return obj


class TrialView(View):
    http_method_names = ['post', 'head']

    def head(*args, **kwargs):
        response = HttpResponse(status=200)
        response['Access-Control-Allow-Origin'] = '*'
        return response

    def post(self, request, *args, **kwargs):
        try:
            trial = json.loads(request.body, object_hook=datetime_decoder)
            Trial.add(**trial)
            response = JsonResponse({'code':200, 'status':'OK', 'message': 'Trial added to the database.'}, status=201)
        except json.decoder.JSONDecodeError:
            response = JsonResponse({'code':400, 'status':'Bad Request', 'message': 'JSON Decode Error'}, status=400)

        response['Access-Control-Allow-Origin'] = '*'
        return response
