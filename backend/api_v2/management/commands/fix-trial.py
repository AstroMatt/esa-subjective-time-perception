import sys
import datetime
import json
from django.db import IntegrityError
from json.decoder import JSONDecodeError
from django.core.management.base import BaseCommand
from backend.api_v2.models import Click
from backend.api_v2.models import Event
from backend.api_v2.models import Trial
from backend.api_v2.models import Survey
from backend.logger.models import HTTPRequest


def decode_json(obj):
    for key, value in obj.items():
        if 'datetime' in key:
            obj[key] = datetime.datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%fZ').replace(tzinfo=datetime.timezone.utc)
        elif key == 'colors':
            obj[key] = ','.join(value)
    return obj


def get_data(request):
    try:
        return json.loads(request, object_hook=decode_json)
    except JSONDecodeError:
        print(f'JSON decode error: {data.sha1}')
        sys.exit(1)


def save_data(http_request_sha1, trial, survey, clicks, events):
    try:
        trial = Trial.objects.create(http_request_sha1=http_request_sha1, **trial)

        if survey:
            Survey.objects.create(trial=trial, **survey)

        for click in clicks:
            Click.objects.create(trial=trial, **click)

        for event in events:
            Event.objects.create(trial=trial, **event)

        trial.validate()
        trial.calculate()

        Click.objects.filter(trial=trial).delete()
        Event.objects.filter(trial=trial).delete()

    except IntegrityError:
        print(f'IntegrityError: {sha1}')


def clean():
    Survey.objects.all().delete()
    Click.objects.all().delete()
    Event.objects.all().delete()
    Trial.objects.all().delete()


class Command(BaseCommand):
    help = 'Recalculate whole database.'

    def handle(self, *args, **options):
        for request in HTTPRequest.objects.all():
            data = get_data(request.data)
            save_data(
                http_request_sha1=request.sha1,
                trial=data.get('trial', None),
                survey=data.get('survey', None),
                clicks=data.get('clicks'),
                events=data.get('events'),
            )
