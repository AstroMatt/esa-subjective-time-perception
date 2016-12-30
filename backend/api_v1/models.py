import statistics
from datetime import datetime
from datetime import timezone
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.db import models


class Experiment(models.Model):
    RHYTHMS = [
        ('perfect', _('Perfect')),
        ('above-average', _('Above average')),
        ('average', _('Average')),
        ('below-average', _('Below average')),
        ('poor', _('Poor'))]
    GENDERS = [
        ('female', _('Female')),
        ('male', _('Male')),
        ('other', _('Other'))]
    CONDITIONS = [
        ('well-rested', _('Well rested')),
        ('normal', _('Normal')),
        ('tired', _('Tired'))]

    location = models.CharField(max_length=50)
    experiment_start = models.DateTimeField(null=True)
    experiment_end = models.DateTimeField(null=True)
    timeout = models.PositiveIntegerField(help_text=_('Microseconds'))
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    #email = models.EmailField(null=True, blank=True)
    age = models.PositiveSmallIntegerField()
    #attempt = models.PositiveSmallIntegerField()
    rhythm = models.CharField(max_length=50, choices=RHYTHMS)
    gender = models.CharField(max_length=50, choices=GENDERS)
    condition = models.CharField(max_length=50, choices=CONDITIONS)
    is_valid = models.NullBooleanField(null=True)

    DEVICES = [
        ('computer-1', _('Computer 1')),
        ('computer-2', _('Computer 2'))]
    POLARIZATIONS = [
        ('horizontal', _('Horizontal')),
        ('vertical', _('Vertical')),
        ('cross', _('Cross')),
        ('mixed', _('Mixed'))]
    polarization = models.CharField(max_length=15, choices=POLARIZATIONS)
    device = models.CharField(max_length=50, choices=DEVICES)
    order = models.CharField(max_length=70, null=True)

    white_start = models.DateTimeField(null=True)
    white_end = models.DateTimeField(null=True)
    blue_start = models.DateTimeField(null=True)
    blue_end = models.DateTimeField(null=True)
    red_start = models.DateTimeField(null=True)
    red_end = models.DateTimeField(null=True)
    is_valid = models.NullBooleanField(null=True)

    @staticmethod
    def get():
        return Experiment.objects.filter(is_valid=True)

    def get_clicks_valid_for_experiment(self):
        clicks = Click.objects.filter(experiment=self).order_by('datetime')
        blue = list(clicks.filter(background='blue'))[5:-5]
        red = list(clicks.filter(background='red'))[5:-5]
        white = list(clicks.filter(background='white'))[5:-5]

        return {
            'all': blue + red + white,
            'blue': blue,
            'red': red,
            'white': white}

    def count_clicks(self):
        clicks = Click.objects.filter(experiment=self)

        return {
            'all': clicks.count(),
            'blue': clicks.filter(background='blue').count(),
            'red': clicks.filter(background='red').count(),
            'white': clicks.filter(background='white').count()}

    def regularity_coefficient_percent(self):
        clicks = Click.objects.filter(experiment=self)

        return {
            'all': clicks.count() / 90 * 100,
            'blue': clicks.filter(background='blue').count() / 30 * 100,
            'red': clicks.filter(background='red').count() / 30 * 100,
            'white': clicks.filter(background='white').count() / 30 * 100}

    def regularity_coefficient_time(self):
        clicks = self.get_clicks_valid_for_experiment()

        def get_time_deltas(series):

            for i in range(1, len(series)):
                d1 = series[i-1].datetime
                d2 = series[i].datetime
                yield (d2 - d1).total_seconds()

        blue = list(get_time_deltas(clicks['blue']))
        red = list(get_time_deltas(clicks['red']))
        white = list(get_time_deltas(clicks['white']))

        return {
            'all': blue + red + white,
            'blue': blue,
            'red': red,
            'white': white}

    def stdev(self):
        clicks = self.regularity_coefficient_time()

        def stdev(series):
            try:
                return statistics.stdev(series)
            except statistics.StatisticsError:
                return None

        return {
            'all': stdev(clicks['all']),
            'blue': stdev(clicks['blue']),
            'red': stdev(clicks['red']),
            'white': stdev(clicks['white'])}

    def mean(self):
        clicks = self.regularity_coefficient_time()

        def mean(series):
            try:
                return statistics.mean(series)
            except statistics.StatisticsError:
                return None

        return {
            'all': mean(clicks['all']),
            'blue': mean(clicks['blue']),
            'red': mean(clicks['red']),
            'white': mean(clicks['white'])}

    def add(**data):



        raise KeyError
        return



        experiment, status = Experiment.objects.get_or_create(
            date=date_of_experiment,
            location=data.get('location'),
            polarization=data.get('polarization'),
            device=data.get('device'),
            first_name=data.get('first_name').title(),
            last_name=data.get('last_name').title(),
            timeout=data.get('timeout'),
            age=data.get('age'),
            gender=data.get('gender'),
            rhythm=data.get('rhythm'),
            condition=data.get('condition'))

        for event in data.get('events'):
            Event.objects.get_or_create(
                experiment=experiment,
                datetime=make_datetime(event.get('datetime')),
                action=event.get('action'),
                message=event.get('message'))

        for click in data.get('clicks'):
            Click.objects.get_or_create(
                experiment=experiment,
                datetime=make_datetime(click.get('datetime')),
                background=click.get('background'))
        return experiment

    def __str__(self):
        return f'[{self.experiment_start:%Y-%m-%d %H:%M}] {self.location} ({self.device}, {self.polarization}) {self.first_name} {self.last_name}'

    class Meta:
        ordering = ['last_name', 'first_name', 'age', '-experiment_start']
        verbose_name = _('Experiment')
        verbose_name_plural = _('Experiments')
        db_table = 'experiment_experiment'


class Trial(models.Model):
    DEVICES = [
        ('computer-1', _('Computer 1')),
        ('computer-2', _('Computer 2'))]
    POLARIZATIONS = [
        ('horizontal', _('Horizontal')),
        ('vertical', _('Vertical')),
        ('cross', _('Cross')),
        ('mixed', _('Mixed'))]

    experiment = models.ForeignKey(to='api_v1.Experiment')
    polarization = models.CharField(max_length=15, choices=POLARIZATIONS)
    device = models.CharField(max_length=50, choices=DEVICES)
    order = models.CharField(max_length=70, null=True)
    start = models.DateTimeField(null=True)
    end = models.DateTimeField(null=True)
    white_start = models.DateTimeField(null=True)
    white_end = models.DateTimeField(null=True)
    blue_start = models.DateTimeField(null=True)
    blue_end = models.DateTimeField(null=True)
    red_start = models.DateTimeField(null=True)
    red_end = models.DateTimeField(null=True)
    is_valid = models.NullBooleanField(null=True)

    @staticmethod
    def get():
        return Trial.objects.filter(is_valid=True)

    def __str__(self):
        return '[{start}]'.format(**self.__dict__)

    class Meta:
        ordering = ['-start']
        verbose_name = _('Trial')
        verbose_name_plural = _('Trials')
        db_table = 'experiment_trial'


class Click(models.Model):
    EXPECTED_COUNT = 90
    BACKGROUNDS = [
        ('black', _('Black')),
        ('white', _('White')),
        ('blue', _('Blue')),
        ('red', _('Red'))]
    experiment = models.ForeignKey(to='api_v1.Experiment')
    datetime = models.DateTimeField()
    background = models.CharField(max_length=15, choices=BACKGROUNDS)

    def __str__(self):
        return f'[{self.datetime:%Y-%m-%d %H:%M}] clicked background {self.background}'

    class Meta:
        ordering = ['datetime']
        verbose_name = _('Click event')
        verbose_name_plural = _('Click events')
        db_table = 'experiment_click'


class Event(models.Model):
    ACTIONS = [
        ('start', _('Start')),
        ('end', _('End'))]
    experiment = models.ForeignKey(to='api_v1.Experiment')
    datetime = models.DateTimeField()
    action = models.CharField(max_length=15, choices=ACTIONS)
    message = models.CharField(max_length=30)

    def __str__(self):
        return f'[{self.datetime:%Y-%m-%d %H:%M}] - {self.message} - {self.action}'

    class Meta:
        ordering = ['datetime']
        verbose_name = _('Event')
        verbose_name_plural = _('Events')
        db_table = 'experiment_event'
