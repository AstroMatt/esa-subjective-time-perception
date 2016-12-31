from django.db import models
from django.db.models import DateTimeField
from django.db.models import CharField
from django.db.models import ForeignKey
from django.db.models import NullBooleanField
from django.utils.translation import ugettext_lazy as _


class Event(models.Model):
    trial = ForeignKey(verbose_name=_('Trial'), to='api_v2.Trial', db_index=True)
    datetime = DateTimeField(verbose_name=_('Datetime'), db_index=True)
    target = CharField(verbose_name=_('Target'), max_length=50, db_index=True)
    action = CharField(verbose_name=_('Action'), max_length=50, db_index=True)

    class Meta:
        verbose_name = _('Event')
        verbose_name_plural = _('Events')

    def __str__(self):
        return f'[{self.datetime:%Y-%m-%d %H:%M}] {self.target}: {self.action}'
