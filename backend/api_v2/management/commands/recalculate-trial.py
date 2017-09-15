import logging
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.core.management.base import BaseCommand
from backend.api_v2.models import Click
from backend.api_v2.models import Event
from backend.api_v2.models import Trial
from backend.api_v2.models import Survey
from backend.api_v2.utils import json_decode
from backend.logger.models import HTTPRequest


class Command(BaseCommand):
    help = 'Recalculate Trials.'

    def add_arguments(self, parser):
        parser.add_argument(
            '--all',
            action='store_true',
            default=False,
            help='Recalculate all trials',
        )

    def handle(self, *args, **options):
        if options['all']:
            requests_to_recalculate = HTTPRequest.objects.all()
            Survey.objects.all().delete()
            Click.objects.all().delete()
            Event.objects.all().delete()
            Trial.objects.all().delete()
        else:
            hashes = list(Trial.objects.filter(regularity_all__isnull=True).values_list('http_request_sha1', flat=True))
            requests_to_recalculate = HTTPRequest.objects.filter(sha1__in=hashes)

        for request in requests_to_recalculate:
            data = json_decode(request.data)

            try:
                Trial.add(
                    http_request_sha1=request.sha1,
                    trial=data.get('trial', None),
                    surveys=data.get('survey', None),
                    clicks=data.get('clicks', None),
                    events=data.get('events', None),
                )

            except IntegrityError as e:
                logging.warning(f'{request.sha1} IntegrityError: {e}')

            except ValidationError as e:
                logging.error(f'{request.sha1} ValidationError: {e}')

            except ValueError as e:
                logging.error(f'{request.sha1} ValueError: {e}')

        Click.objects.all().delete()
        Event.objects.all().delete()
