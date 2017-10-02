from django.core.management.base import BaseCommand
from backend.api_v2.models import Click
from backend.api_v2.models import Event


class Command(BaseCommand):
    help = 'Clean Click and Event in the database.'

    def handle(self, *args, **options):
        Click.objects.all().delete()
        Event.objects.all().delete()
