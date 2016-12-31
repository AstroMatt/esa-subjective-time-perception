from django.db import models
from django.db.models import CharField
from django.db.models import DateTimeField
from django.db.models import EmailField
from django.db.models import NullBooleanField
from django.utils.translation import ugettext_lazy as _


class Experiment(models.Model):
    is_valid = NullBooleanField(default=None)

    uid = EmailField(db_index=True)
    location = CharField(max_length=50, db_index=True)
    device = CharField(max_length=50)

    start = DateTimeField(db_index=True, null=True, blank=True)
    end = DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.uid}'
