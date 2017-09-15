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


def get_survey(survey):
    out = {}
    for key, value in survey.items():
        if not value:
            value = None
        out[key] = value
    return out


def save_data(http_request_sha1, trial, survey, clicks, events):
    try:
        trial, _ = Trial.objects.get_or_create(http_request_sha1=http_request_sha1, defaults=trial)

        if survey:
            Survey.objects.get_or_create(trial=trial, **get_survey(survey))

        for click in clicks:
            Click.objects.get_or_create(trial=trial, **click)

        for event in events:
            Event.objects.get_or_create(trial=trial, **event)

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


def from_everywhere():
    return HTTPRequest.objects.all()


def from_trial():
    hashes = list(Trial.objects.filter(regularity_all__isnull=True).values_list('http_request_sha1', flat=True))
    return HTTPRequest.objects.filter(sha1__in=hashes)


class Command(BaseCommand):
    help = 'Recalculate whole database.'

    def handle(self, *args, **options):
        Survey.objects.all().delete()
        Click.objects.all().delete()
        Event.objects.all().delete()
        Trial.objects.all().delete()

        for request in from_everywhere():
            data = get_data(request.data)
            save_data(
                http_request_sha1=request.sha1,
                trial=data.get('trial', None),
                survey=data.get('survey', None),
                clicks=data.get('clicks', None),
                events=data.get('events', None),
            )

        Click.objects.all().delete()
        Event.objects.all().delete()
