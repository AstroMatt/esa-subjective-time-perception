from django.db import models
from django.db.models import DateTimeField
from django.db.models import CharField
from django.db.models import FloatField
from django.db.models import ForeignKey
from django.db.models import EmailField
from django.db.models import PositiveSmallIntegerField
from django.utils.translation import ugettext_lazy as _

from backend.api_v2.models import Click
from backend.api_v2.models import Event
from backend.api_v2.models import Survey


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

    # Count click events
    count_all = PositiveSmallIntegerField(verbose_name=('C'), help_text=_('Count click events - all'), null=True, blank=True)
    count_blue = PositiveSmallIntegerField(verbose_name=('CB'), help_text=_('Count click events - blue'), null=True, blank=True)
    count_red = PositiveSmallIntegerField(verbose_name=('CR'), help_text=_('Count click events - red'), null=True, blank=True)
    count_white = PositiveSmallIntegerField(verbose_name=('CW'), help_text=_('Count click events - white'), null=True, blank=True)

    # Percentage cefficient for 80% of median intervals
    percentage_all = FloatField(verbose_name=('P'), help_text=_('Percentage Coefficient - all'), null=True, blank=True)
    percentage_blue = FloatField(verbose_name=('PB'), help_text=_('Percentage Coefficient - blue'), null=True, blank=True)
    percentage_red = FloatField(verbose_name=('PR'), help_text=_('Percentage Coefficient - red'), null=True, blank=True)
    percentage_white = FloatField(verbose_name=('PW'), help_text=_('Percentage Coefficient - white'), null=True, blank=True)

    # Time Coefficient Standard Deviation of 80% median intervals
    time_stdev_all = FloatField(verbose_name=('TSD'), help_text=_('Time Coefficient Standard Deviation - all'), null=True, blank=True)
    time_stdev_blue = FloatField(verbose_name=('TSDB'), help_text=_('Time Coefficient Standard Deviation - blue'), null=True, blank=True)
    time_stdev_red = FloatField(verbose_name=('TSDR'), help_text=_('Time Coefficient Standard Deviation - red'), null=True, blank=True)
    time_stdev_white = FloatField(verbose_name=('TSDW'), help_text=_('Time Coefficient Standard Deviation - white'), null=True, blank=True)

    # Time Coefficient Mean of 80% median intervals
    time_mean_all = FloatField(verbose_name=('TM'), help_text=_('Time Coefficient Mean - all'), null=True, blank=True)
    time_mean_blue = FloatField(verbose_name=('TMB'), help_text=_('Time Coefficient Mean - blue'), null=True, blank=True)
    time_mean_red = FloatField(verbose_name=('TMR'), help_text=_('Time Coefficient Mean - red'), null=True, blank=True)
    time_mean_white = FloatField(verbose_name=('TMW'), help_text=_('Time Coefficient Mean - white'), null=True, blank=True)

    def __str__(self):
        return f'[{self.start_datetime:%Y-%m-%d %H:%M}] {self.location} ({self.device}, {self.polarization}), {self.uid}, attempt: {self.attempt}'

    class Meta:
        verbose_name = _('Trial')
        verbose_name_plural = _('Trials')

    def validate_clicks(self, color, margin=0.2):
        margin = round(self.timeout / self.regularity * margin)

        clicks = Click.objects.filter(trial=self).order_by('datetime')
        valid = list(clicks.filter(target=color))[margin:-margin]
        invalid_left = list(clicks.filter(target=color))[:margin]
        invalid_right = list(clicks.filter(target=color))[-margin:]

        for event in valid:
            event.is_valid = True
            event.save()

        for event in invalid_left + invalid_right:
            event.is_valid = False
            event.save()


    def count_clicks(self):
        clicks = Click.objects.filter(trial=self, is_valid=True)
        self.count_all = clicks.all().count()
        self.count_blue = clicks.filter(color='blue').count()
        self.count_red = clicks.filter(color='red').count()
        self.count_white = clicks.filter(color='white').count()
        self.save()


    def calculate(self):
        self.validate_clicks('blue')
        self.validate_clicks('red')
        self.validate_clicks('white')
        self.count_clicks()




        print('percentage_all', self.percentage_all)
        print('percentage_blue', self.percentage_blue)
        print('percentage_red', self.percentage_red)
        print('percentage_white', self.percentage_white)








    def regularity_coefficient_percent(self):
        clicks = Click.objects.filter(experiment=self)

        return {
            'all': clicks.count() / 90 * 100,
            'blue': clicks.filter(background='blue').count() / 30 * 100,
            'red': clicks.filter(background='red').count() / 30 * 100,
            'white': clicks.filter(background='white').count() / 30 * 100}
