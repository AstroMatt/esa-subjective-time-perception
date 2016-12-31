from django.db import models
from django.db.models import DateTimeField
from django.db.models import CharField
from django.db.models import ForeignKey
from django.utils.translation import ugettext_lazy as _


class Event(models.Model):
    trial = ForeignKey(to='api_v2.Trial', db_index=True)
    datetime = DateTimeField()
    target = CharField(max_length=50, db_index=True)
    action = CharField(max_length=50, db_index=True)

    def __str__(self):
        return f'[{self.datetime:%Y-%m-%d %H:%M}] {self.target}: {self.action}'
