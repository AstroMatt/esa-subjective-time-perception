import datetime
import json
from json.decoder import JSONDecodeError

from django.db.utils import IntegrityError
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.generic import View

from backend.api_v2.models import Event
from backend.api_v2.models import Trial
from backend.api_v2.models import Survey
from backend.logger.models import RequestLogger


def decode_json(obj):
    for key, value in obj.items():
        if 'datetime' in key:
           obj[key] = datetime.datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%fZ').replace(tzinfo=datetime.timezone.utc)
        elif key == 'colors':
            obj[key] = ','.join(value)
    return obj


class APIv2View(View):
    http_method_names = ['post', 'head']

    def head(self, request, *args, **kwargs):
        RequestLogger.add(request, api_version=2)
        response = HttpResponse(status=200)
        response['Access-Control-Allow-Origin'] = '*'
        return response

    def post(self, request, *args, **kwargs):
        try:
            RequestLogger.add(request, api_version=2)
            data = json.loads(request.body, object_hook=decode_json)
            trial, _ = Trial.objects.get_or_create(**data.get('trial'))

            if data.get('survey'):
                Survey.objects.get_or_create(trial=trial, **data.get('survey'))

            for event in data.get('events'):
                Event.objects.get_or_create(trial=trial, **event)

            response = JsonResponse({'code':201, 'status':'OK', 'message': 'Trial added to the database.'}, status=201)
        except JSONDecodeError:
            response = JsonResponse({'code':400, 'status':'Bad Request', 'message': 'JSON decode error'}, status=400)
        except IntegrityError:
            response = JsonResponse({'code':400, 'status':'Bad Request', 'message': 'Integrity error'}, status=400)

        response['Access-Control-Allow-Origin'] = '*'
        return response
