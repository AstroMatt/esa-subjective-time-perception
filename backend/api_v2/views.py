import datetime
import json
from json.decoder import JSONDecodeError

from django.db.utils import IntegrityError
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.generic import View

from backend.api_v2.models import Click
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
    http_method_names = ['get', 'post', 'head', 'update', 'patch']

    def patch(self, request, *args, **kwargs):
        RequestLogger.add(request, api_version=2)
        id = request.GET.get('id')
        Trial.objects.get(id=id).validate()
        Trial.objects.get(id=id).calculate()
        response = HttpResponse(status=200)
        response['Access-Control-Allow-Origin'] = '*'
        return response

    def update(self, request, *args, **kwargs):
        RequestLogger.add(request, api_version=2)

        for t in Trial.objects.all():
            t.validate()
            t.calculate()

        response = HttpResponse(status=200)
        response['Access-Control-Allow-Origin'] = '*'
        return response

    def head(self, request, *args, **kwargs):
        RequestLogger.add(request, api_version=2)
        response = HttpResponse(status=200)
        response['Access-Control-Allow-Origin'] = '*'
        return response

    def post(self, request, *args, **kwargs):
        RequestLogger.add(request, api_version=2)

        try:
            data = json.loads(request.body, object_hook=decode_json)
            trial, _ = Trial.objects.get_or_create(**data.get('trial'))

            if data.get('survey'):
                Survey.objects.get_or_create(trial=trial, **data.get('survey'))

            for click in data.get('clicks'):
                Click.objects.get_or_create(trial=trial, **click)

            for event in data.get('events'):
                Event.objects.get_or_create(trial=trial, **event)

            trial.validate()
            trial.calculate()
            data = [field for field in trial.__dict__ if not field.startswith('_')]
            response = JsonResponse({'code':200, 'status':'OK', 'message': 'Trial added to the database.', 'data': json.dumps(data)}, status=200)
        except JSONDecodeError:
            response = JsonResponse({'code':400, 'status':'Bad Request', 'message': 'JSON decode error'}, status=400)
        except IntegrityError:
            response = JsonResponse({'code':400, 'status':'Bad Request', 'message': 'Integrity error'}, status=400)

        response['Access-Control-Allow-Origin'] = '*'
        return response

    def get(self, request, *args, **kwargs):
        start_datetime = datetime.datetime.strptime(request.GET['start_datetime'], '%Y-%m-%dT%H:%M:%S.%f')
        try:
            trial = Trial.objects.get(start_datetime__startswith=start_datetime)
            data = [field for field in trial.__dict__ if not field.startswith('_')]
            response = JsonResponse({'code':200, 'status':'OK', 'data': json.dumps(data)}, status=200)
        except Trial.DoesNotExist:
            response = JsonResponse({'code':400, 'status':'Bad Request', 'message': 'Integrity error'}, status=400)

        response['Access-Control-Allow-Origin'] = '*'
        return response
