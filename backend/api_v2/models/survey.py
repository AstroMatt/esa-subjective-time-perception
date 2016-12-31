from django.db import models
from django.db.models import CharField
from django.db.models import DateTimeField
from django.db.models import EmailField
from django.db.models import ForeignKey
from django.db.models import PositiveSmallIntegerField
from django.utils.translation import ugettext_lazy as _


class Survey(models.Model):
    trial = ForeignKey(to='api_v2.Trial', db_index=True)
    datetime = DateTimeField()
    email = EmailField(db_index=True)
    age = PositiveSmallIntegerField()
    condition = CharField(max_length=50)
    gender = CharField(max_length=50)
    rhythm = CharField(max_length=50)

    def __str__(self):
        return f'{self.datetime}'
