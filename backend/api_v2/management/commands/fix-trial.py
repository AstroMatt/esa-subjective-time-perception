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


def add_data(data, sha1):
    try:
        data = json.loads(data, object_hook=decode_json)
    except JSONDecodeError:
        print(f'JSON decode error: {data.sha1}')

    trial_data = data.get('trial')
    start_datetime = trial_data.get('start_datetime')
    trial_data.pop('start_datetime', None)
    trial_data.update(
        time=data.get('survey', {}).get('time'),
        http_request_sha1=sha1,
    )

    try:
        trial, _ = Trial.objects.get_or_create(start_datetime=start_datetime, defaults=trial_data)
        print(f'SHA1: {sha1:.7}, trial: {trial}')

        if data.get('survey'):
            Survey.objects.get_or_create(trial=trial, **data.get('survey'))

        for click in data.get('clicks'):
            Click.objects.get_or_create(trial=trial, **click)

        for event in data.get('events'):
            Event.objects.get_or_create(trial=trial, **event)

        trial.validate()
        trial.calculate()

        #Click.objects.filter(trial=trial).delete()
        #Event.objects.filter(trial=trial).delete()

    except IntegrityError:
        print(f'IntegrityError: {data.sha1}')


class Command(BaseCommand):
    help = 'Clean Click and Event in the database.'

    def handle(self, *args, **options):
        for request in HTTPRequest.objects.all():
            if not Trial.objects.filter(http_request_sha1=request.sha1).count():
                add_data(data=request.data, sha1=request.sha1)

