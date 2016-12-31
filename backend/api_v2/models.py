from django.db import models
from django.db.models import DateTimeField
from django.db.models import CharField
from django.db.models import FloatField
from django.db.models import ForeignKey
from django.db.models import EmailField
from django.db.models import PositiveSmallIntegerField
from django.utils.translation import ugettext_lazy as _


class Event(models.Model):
    trial = ForeignKey(verbose_name=_('Trial'), to='api_v2.Trial', db_index=True)
    datetime = DateTimeField(verbose_name=_('Datetime'), db_index=True)
    target = CharField(verbose_name=_('Target'), max_length=50, db_index=True)
    action = CharField(verbose_name=_('Action'), max_length=50, db_index=True)

    def __str__(self):
        return f'[{self.datetime:%Y-%m-%d %H:%M}] {self.target}: {self.action}'

    class Meta:
        ordering = ['-datetime']
        verbose_name = _('Event')
        verbose_name_plural = _('Events')


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
        ordering = ['-datetime']
        verbose_name = _('Survey')
        verbose_name_plural = _('Surveys')


class Trial(models.Model):
    start_datetime = DateTimeField(verbose_name=_('Start datetime'), db_index=True)
    end_datetime = DateTimeField(verbose_name=_('End datetime'))
    colors = CharField(verbose_name=_('Color order'), max_length=50)
    device = CharField(verbose_name=_('Device'), max_length=50)
    location = CharField(verbose_name=_('Location'), max_length=50, db_index=True)
    uid = EmailField(verbose_name=_('User ID'), db_index=True)
    polarization = CharField(verbose_name=_('Polarization'), max_length=50)
    timeout = FloatField(verbose_name=_('Timeout'), help_text=_('Seconds per color'))
    regularity = PositiveSmallIntegerField(verbose_name=_('Reqularity'), help_text=_('Click every X seconds'))
    attempt = PositiveSmallIntegerField(verbose_name=_('Attempt'), db_index=True)

    def __str__(self):
        return f'[{self.start_datetime:%Y-%m-%d %H:%M}] {self.location} ({self.device}, {self.polarization}), {self.uid}, attempt: {self.attempt}'

    class Meta:
        ordering = ['-start_datetime']
        verbose_name = _('Trial')
        verbose_name_plural = _('Trials')
