from django.db import models
from django.db.models import DateTimeField
from django.db.models import CharField
from django.db.models import ForeignKey
from django.db.models import EmailField
from django.db.models import PositiveSmallIntegerField
from django.utils.translation import ugettext_lazy as _


class Survey(models.Model):
    trial = ForeignKey(verbose_name=_('Trial'), to='api_v2.Trial', db_index=True)
    datetime = DateTimeField(verbose_name=_('Datetime'))
    email = EmailField(verbose_name=_('Email'), db_index=True)
    age = PositiveSmallIntegerField(verbose_name=_('Age'))
    condition = CharField(verbose_name=_('Condition'), max_length=50)
    gender = CharField(verbose_name=_('Gender'), max_length=50)
    rhythm = CharField(verbose_name=_('Rhythm'), max_length=50)

    def __str__(self):
        return f'{self.datetime}'

    class Meta:
        verbose_name = _('Survey')
        verbose_name_plural = _('Surveys')
