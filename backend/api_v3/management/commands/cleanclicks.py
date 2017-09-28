from django.core.management.base import BaseCommand
from backend.api_v3.models import Click


class Command(BaseCommand):
    help = 'Clean Click and Event in the database.'

    def handle(self, *args, **options):
        Click.objects.all().delete()
