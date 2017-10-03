import json
import logging

from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.core.management.base import BaseCommand
from django.core.serializers import deserialize

from backend._common.utils import json_datetime_decoder
from backend.logger.models import HTTPRequest
from backend.api_v3.models import Click
from backend.api_v3.models import Result


logging.basicConfig(
    level=logging.DEBUG,
    format='[%(asctime).19s] %(levelname)s %(message)s',
)


class Command(BaseCommand):
    help = 'Recalculate results.'

    def add_arguments(self, parser):
        parser.add_argument(
            '--all',
            action='store_true',
            default=False,
            help='Recalculate all results',
        )

    def handle(self, *args, **options):
        requests_to_recalculate = HTTPRequest.objects.filter(api_version=3)

        if options['all']:
            Click.objects.all().delete()
            Result.objects.all().delete()
        else:
            todo = []
            invalid = list(Result.objects.filter(regularity_all__isnull=True).values_list('request_sha1', flat=True))
            valid = list(Result.objects.all().values_list('request_sha1', flat=True))

            for req in list(HTTPRequest.objects.all().values_list('sha1', flat=True)):
                if req in invalid or req not in valid:
                    todo.append(req)

            requests_to_recalculate = requests_to_recalculate.filter(sha1__in=todo)

        self.recalculate(requests_to_recalculate)

    def recalculate(self, requests_to_recalculate):
        logging.info(f'Will recalculate: {requests_to_recalculate}')

        for request in requests_to_recalculate:
            logging.info(f'{request}')

            try:
                data = json.loads(request.data, object_hook=json_datetime_decoder)
            except TypeError as e:
                logging.error(f'{request.sha1} JSON decode error: {e}')

            try:
                Result.add(
                    request_sha1=request.sha1,
                    clicks=data.pop('clicks'),
                    result=data,
                )

            except IntegrityError as e:
                logging.warning(f'{request.sha1} IntegrityError: {e}')

            except ValidationError as e:
                logging.error(f'{request.sha1} ValidationError: {e}')

            except ValueError as e:
                logging.error(f'{request.sha1} ValueError: {e}')

        Click.objects.all().delete()
