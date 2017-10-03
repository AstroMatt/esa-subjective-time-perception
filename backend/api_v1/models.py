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

    DEVICES = [
        ('computer-1', _('Computer 1')),
        ('computer-2', _('Computer 2'))]

    POLARIZATIONS = [
        ('horizontal', _('Horizontal')),
        ('vertical', _('Vertical')),
        ('cross', _('Cross')),
        ('mixed', _('Mixed'))]

    location = models.CharField(verbose_name=_('Location'), max_length=50)
    experiment_start = models.DateTimeField(verbose_name=_('Start date'), null=True)
    experiment_end = models.DateTimeField(verbose_name=_('End date'), null=True)
    timeout = models.PositiveIntegerField(verbose_name=_('Timeout'), help_text=_('Microseconds'))
    first_name = models.CharField(verbose_name=_('First name'), max_length=50, null=True)
    last_name = models.CharField(verbose_name=_('Last name'), max_length=50, null=True)
    age = models.PositiveSmallIntegerField(verbose_name=_('Age'), )
    rhythm = models.CharField(verbose_name=_('Rhythm'), max_length=50, choices=RHYTHMS)
    gender = models.CharField(verbose_name=_('Gender'), max_length=50, choices=GENDERS)
    condition = models.CharField(verbose_name=_('Condition'), max_length=50, choices=CONDITIONS)
    is_valid = models.NullBooleanField(verbose_name=_('Is valid?'), null=True)

    polarization = models.CharField(verbose_name=_('Polarization'), max_length=15, choices=POLARIZATIONS)
    device = models.CharField(verbose_name=_('Device'), max_length=50, choices=DEVICES)
    order = models.CharField(verbose_name=_('Order'), max_length=70, null=True)

    white_start = models.DateTimeField(verbose_name=_('White color start'), null=True)
    white_end = models.DateTimeField(verbose_name=_('White color end'), null=True)
    blue_start = models.DateTimeField(verbose_name=_('Blue color start'), null=True)
    blue_end = models.DateTimeField(verbose_name=_('Blue color end'), null=True)
    red_start = models.DateTimeField(verbose_name=_('Red color start'), null=True)
    red_end = models.DateTimeField(verbose_name=_('Red color end'), null=True)
    is_valid = models.NullBooleanField(verbose_name=_('Is valid?'), null=True)

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
                d1 = series[i - 1].datetime
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

    def __str__(self):
        return f'[{self.experiment_start:%Y-%m-%d %H:%M}] {self.location} ({self.device}, {self.polarization}) {self.first_name} {self.last_name}'

    class Meta:
        verbose_name = _('Experiment')
        verbose_name_plural = _('Experiments')


class Trial(models.Model):
    DEVICES = [
        ('computer-1', _('Computer 1')),
        ('computer-2', _('Computer 2'))]
    POLARIZATIONS = [
        ('horizontal', _('Horizontal')),
        ('vertical', _('Vertical')),
        ('cross', _('Cross')),
        ('mixed', _('Mixed'))]

    experiment = models.ForeignKey(verbose_name=_('Experiment'), to='api_v1.Experiment')
    polarization = models.CharField(verbose_name=_('Polarization'), max_length=15, choices=POLARIZATIONS)
    device = models.CharField(verbose_name=_('Device'), max_length=50, choices=DEVICES)
    order = models.CharField(verbose_name=_('Order'), max_length=70, null=True)
    start = models.DateTimeField(verbose_name=_('Start date'), null=True)
    end = models.DateTimeField(verbose_name=_('End date'), null=True)
    white_start = models.DateTimeField(verbose_name=_('White color start'), null=True)
    white_end = models.DateTimeField(verbose_name=_('White color end'), null=True)
    blue_start = models.DateTimeField(verbose_name=_('Blue color start'), null=True)
    blue_end = models.DateTimeField(verbose_name=_('Blue color end'), null=True)
    red_start = models.DateTimeField(verbose_name=_('Red color start'), null=True)
    red_end = models.DateTimeField(verbose_name=_('Red color end'), null=True)
    is_valid = models.NullBooleanField(verbose_name=_('Is valid?'), null=True)

    @staticmethod
    def get():
        return Trial.objects.filter(is_valid=True)

    def __str__(self):
        return '[{start}]'.format(**self.__dict__)

    class Meta:
        verbose_name = _('Trial')
        verbose_name_plural = _('Trials')


class Click(models.Model):
    EXPECTED_COUNT = 90
    BACKGROUNDS = [
        ('black', _('Black')),
        ('white', _('White')),
        ('blue', _('Blue')),
        ('red', _('Red'))]
    experiment = models.ForeignKey(verbose_name=_('Experiment'), to='api_v1.Experiment')
    datetime = models.DateTimeField(verbose_name=_('Datetime'), )
    background = models.CharField(verbose_name=_('Background'), max_length=15, choices=BACKGROUNDS)

    def __str__(self):
        return f'[{self.datetime:%Y-%m-%d %H:%M}] clicked background {self.background}'

    class Meta:
        verbose_name = _('Click event')
        verbose_name_plural = _('Click events')


class Event(models.Model):
    ACTIONS = [
        ('start', _('Start')),
        ('end', _('End'))]
    experiment = models.ForeignKey(verbose_name=_('Experiment'), to='api_v1.Experiment')
    datetime = models.DateTimeField(verbose_name=_('Datetime'))
    action = models.CharField(verbose_name=_('Action'), max_length=15, choices=ACTIONS)
    message = models.CharField(verbose_name=_('Message'), max_length=30)

    def __str__(self):
        return f'[{self.datetime:%Y-%m-%d %H:%M}] - {self.message} - {self.action}'

    class Meta:
        verbose_name = _('Event')
        verbose_name_plural = _('Events')
