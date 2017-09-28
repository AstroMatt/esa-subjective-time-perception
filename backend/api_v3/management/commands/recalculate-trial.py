import logging

from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.core.management.base import BaseCommand

from backend._common.utils import json_decode
from backend.logger.models import HTTPRequest
from backend.api_v3.models import Click
from backend.api_v3.models import Result


logging.basicConfig(
    level=logging.INFO,
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
        if options['all']:
            requests_to_recalculate = HTTPRequest.objects.all()
            Click.objects.all().delete()
            Result.objects.all().delete()
        else:
            todo = []
            invalid = list(Result.objects.filter(regularity_all__isnull=True).values_list('http_request_sha1', flat=True))
            valid = list(Result.objects.all().values_list('http_request_sha1', flat=True))

            for req in list(HTTPRequest.objects.all().values_list('sha1', flat=True)):
                if req in invalid or req not in valid:
                    todo.append(req)

            requests_to_recalculate = HTTPRequest.objects.filter(sha1__in=todo)

        self.stdout.write(f'Will recalculate: {requests_to_recalculate}')

        for request in requests_to_recalculate:
            data = json_decode(request.data)

            try:
                Result.add(
                    http_request_sha1=request.sha1,
                    result=data.get('result', None),
                    clicks=data.get('clicks', None),
                )

            except IntegrityError as e:
                logging.warning(f'{request.sha1} IntegrityError: {e}')

            except ValidationError as e:
                logging.error(f'{request.sha1} ValidationError: {e}')

            except ValueError as e:
                logging.error(f'{request.sha1} ValueError: {e}')

        Click.objects.all().delete()
