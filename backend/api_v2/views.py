import datetime
import json

from django.http import HttpResponse
from django.http import JsonResponse
from django.views.generic import View

from backend.api_v2.models import Event
from backend.api_v2.models import Trial
from backend.api_v2.models import Survey


def clean_json(obj):
    for key, value in obj.items():
        if key in ['datetime', 'start', 'end']:
           obj[key] = datetime.datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%fZ').replace(tzinfo=datetime.timezone.utc)
        if key == 'colors':
            obj[key] = ','.join(value)
    return obj


class APIv2View(View):
    http_method_names = ['post', 'head']

    def head(*args, **kwargs):
        response = HttpResponse(status=200)
        response['Access-Control-Allow-Origin'] = '*'
        return response

    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body, object_hook=clean_json)
            trial, _ = Trial.objects.get_or_create(**data.get('configuration'))

            if data.get('survey'):
                Survey.objects.get_or_create(trial=trial, **data.get('survey'))

            for event in data.get('events'):
                Event.objects.get_or_create(trial=trial, **event)

            response = JsonResponse({'code':200, 'status':'OK', 'message': 'Trial added to the database.'}, status=201)
        except json.decoder.JSONDecodeError:
            response = JsonResponse({'code':400, 'status':'Bad Request', 'message': 'JSON Decode Error'}, status=400)

        response['Access-Control-Allow-Origin'] = '*'
        return response
