import sys
import datetime
import json
import logging
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from json.decoder import JSONDecodeError
from django.core.management.base import BaseCommand
from backend.api_v2.models import Click
from backend.api_v2.models import Event
from backend.api_v2.models import Trial
from backend.api_v2.models import Survey
from backend.logger.models import HTTPRequest


logging.basicConfig(
    level=logging.ERROR,
    format='%(message)s',
    filename='error.log',
)

log = logging.getLogger(__name__)


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

    except IntegrityError as e:
        out = f'{http_request_sha1} IntegrityError: {e}'
        log.warning(out)

    except ValidationError as e:
        out = f'{http_request_sha1} ValidationError: {e}'
        print(out)
        log.error(out)

    except ValueError as e:
        out = f'{http_request_sha1} ValueError: {e}'
        print(out)
        log.error(out)


def clean():
    Survey.objects.all().delete()
    Click.objects.all().delete()
    Event.objects.all().delete()
    Trial.objects.all().delete()


class Command(BaseCommand):
    help = 'Recalculate whole database.'

    def handle(self, *args, **options):

        with open('error.log') as file:
            errors = [line.replace('\n', '') for line in file]

        # for request in HTTPRequest.objects.all():
        for request in HTTPRequest.objects.filter(sha1__in=errors):
            data = get_data(request.data)
            save_data(
                http_request_sha1=request.sha1,
                trial=data.get('trial', None),
                survey=data.get('survey', None),
                clicks=data.get('clicks'),
                events=data.get('events'),
            )
