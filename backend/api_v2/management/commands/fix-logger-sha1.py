from django.core.management.base import BaseCommand
from backend.logger.models import RequestLogger


class Command(BaseCommand):
    help = 'Request Logger calculate SHA1'

    def handle(self, *args, **options):
        for req in RequestLogger.objects.all():
            req.save()
            self.stdout.write(f'id {req.id} sha1: {req.sha1}')

