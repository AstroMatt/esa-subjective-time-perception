from django.db import models
from django.db.models import CharField
from django.db.models import DateTimeField
from django.db.models import EmailField
from django.db.models import FloatField
from django.db.models import ForeignKey
from django.db.models import PositiveSmallIntegerField
from django.db.models import NullBooleanField
from django.utils.translation import ugettext_lazy as _


class Experiment(models.Model):
    participant = EmailField(db_index=True)
    is_valid = NullBooleanField(default=None)


class Trial(models.Model):
    experiment = ForeignKey(to='api_v2.Experiment', null=True, blank=True, db_index=True)

    start = DateTimeField(db_index=True)
    end = DateTimeField()
    colors = CharField(max_length=50, null=True, blank=True)
    device = CharField(max_length=50, null=True, blank=True)
    location = CharField(max_length=50, db_index=True)
    participant = EmailField(db_index=True)
    polarization = CharField(max_length=50)
    seconds = PositiveSmallIntegerField()
    trial = PositiveSmallIntegerField(db_index=True)

    # Count click events
    count_all = PositiveSmallIntegerField(verbose_name=_('Count click events - all'))
    count_blue = PositiveSmallIntegerField(verbose_name=_('Count click events - blue'))
    count_red = PositiveSmallIntegerField(verbose_name=_('Count click events - red'))
    count_white = PositiveSmallIntegerField(verbose_name=_('Count click events - white'))

    # Percentage cefficient for 80% of median intervals
    percentage_all = FloatField(verbose_name=_('Percentage coefficient - all'))
    percentage_blue = FloatField(verbose_name=_('Percentage coefficient - blue'))
    percentage_red = FloatField(verbose_name=_('Percentage coefficient - red'))
    percentage_white = FloatField(verbose_name=_('Percentage coefficient - white'))

    # Time coefficient standard deviation of 80% median intervals
    time_stdev_all = FloatField(verbose_name=_('Time coefficient standard deviation - all'))
    time_stdev_blue = FloatField(verbose_name=_('Time coefficient standard deviation - blue'))
    time_stdev_red = FloatField(verbose_name=_('Time coefficient standard deviation - red'))
    time_stdev_white = FloatField(verbose_name=_('Time coefficient standard deviation - white'))

    # Time coefficient mean of 80% median intervals
    time_mean_all = FloatField(verbose_name=_('Time coefficient mean - all'))
    time_mean_blue = FloatField(verbose_name=_('Time coefficient mean - blue'))
    time_mean_red = FloatField(verbose_name=_('Time coefficient mean - red'))
    time_mean_white = FloatField(verbose_name=_('Time coefficient mean - white'))

    def __str__(self):
        #return f'[{self.start:%Y-%m-%d %H:%M}] {self.location} trial: {self.trial} ({self.device}, {self.polarization}) {self.participant}'
        return f'Trial'

    def calculate_results(self):
        print('Calculating results:', self)

    @staticmethod
    def add(**data):
        #trial, _ = Trial.objects.get_or_create(**data.get('configuration'))
        trial = Trial(**data.get('configuration'))
        print('Add trial', data.get('configuration'))

        if data.get('survey'):
            print('Add survey:', data.get('survey'))
            #Survey.objects.get_or_create(trial=trial, defaults=data.get('survey'))

        for event in data.get('events'):
            print('Add event', event)
            #Event.objects.get_or_create(trial=trial, defaults=event)

        return trial.calculate_results()


class Survey(models.Model):
    #experiment = ForeignKey(to='api_v2.Experiment', null=True, blank=True, db_index=True)
    trial = ForeignKey(to='api_v2.Trial', null=True, blank=True, db_index=True)

    datetime = DateTimeField()
    age = PositiveSmallIntegerField(null=True, blank=True)
    condition = CharField(max_length=50, null=True, blank=True)
    gender = CharField(max_length=50, null=True, blank=True)
    rhythm = CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f'{self.trial}'


class Event(models.Model):
    trial = ForeignKey(to='api_v2.Trial', null=True, blank=True, db_index=True)

    datetime = DateTimeField()
    target = CharField(max_length=50, db_index=True)
    action = CharField(max_length=50, db_index=True)

    def __str__(self):
        return f'[{self.datetime:%Y-%m-%d %H:%M}] {self.target}: {self.action}'
