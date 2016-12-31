from django.db import models
from django.db.models import CharField
from django.db.models import DateTimeField
from django.db.models import EmailField
from django.db.models import FloatField
from django.db.models import NullBooleanField
from django.db.models import PositiveSmallIntegerField
from django.utils.translation import ugettext_lazy as _


class Experiment(models.Model):
    is_valid = NullBooleanField(default=None)
    uid = EmailField(verbose_name=_('User ID'), db_index=True)

    # Trial
    start_datetime = DateTimeField(verbose_name=_('Start datetime'), db_index=True)
    end_datetime = DateTimeField(verbose_name=_('End datetime'))
    location = CharField(verbose_name=_('Location'), max_length=50, db_index=True)
    device = CharField(verbose_name=_('Device'), max_length=50)
    polarization = CharField(verbose_name=_('Polarization'), max_length=50)
    timeout = FloatField(verbose_name=_('Timeout'), help_text=_('Seconds per color'))
    regularity = PositiveSmallIntegerField(verbose_name=_('Reqularity'), help_text=_('Click every X seconds'))

    # Survey
    email = EmailField(verbose_name=_('Email'), db_index=True)
    age = PositiveSmallIntegerField(verbose_name=_('Age'))
    condition = CharField(verbose_name=_('Condition'), max_length=50)
    gender = CharField(verbose_name=_('Gender'), max_length=50)
    rhythm = CharField(verbose_name=_('Rhythm'), max_length=50)

    # Count click events
    count_all_trial1 = PositiveSmallIntegerField(verbose_name=('C_1'), help_text=_('[Trial 1] Count click events - all'), null=True, blank=True)
    count_all_trial2 = PositiveSmallIntegerField(verbose_name=('C_2'), help_text=_('[Trial 2] Count click events - all'), null=True, blank=True)
    count_blue_trial1 = PositiveSmallIntegerField(verbose_name=('CB1'), help_text=_('[Trial 1] Count click events - blue'), null=True, blank=True)
    count_blue_trial2 = PositiveSmallIntegerField(verbose_name=('CB2'), help_text=_('[Trial 2] Count click events - blue'), null=True, blank=True)
    count_red_trial1 = PositiveSmallIntegerField(verbose_name=('CR1'), help_text=_('[Trial 1] Count click events - red'), null=True, blank=True)
    count_red_trial2 = PositiveSmallIntegerField(verbose_name=('CR2'), help_text=_('[Trial 2] Count click events - red'), null=True, blank=True)
    count_white_trial1 = PositiveSmallIntegerField(verbose_name=('CW1'), help_text=_('[Trial 1] Count click events - white'), null=True, blank=True)
    count_white_trial2 = PositiveSmallIntegerField(verbose_name=('CW2'), help_text=_('[Trial 2] Count click events - white'), null=True, blank=True)

    # Percentage cefficient for 80% of median intervals
    percentage_all_trial1 = FloatField(verbose_name=('P_1'), help_text=_('[Trial 1] Percentage Coefficient - all'), null=True, blank=True)
    percentage_all_trial2 = FloatField(verbose_name=('P_2'), help_text=_('[Trial 2] Percentage Coefficient - all'), null=True, blank=True)
    percentage_blue_trial1 = FloatField(verbose_name=('PB1'), help_text=_('[Trial 1] Percentage Coefficient - blue'), null=True, blank=True)
    percentage_blue_trial2 = FloatField(verbose_name=('PB2'), help_text=_('[Trial 2] Percentage Coefficient - blue'), null=True, blank=True)
    percentage_red_trial1 = FloatField(verbose_name=('PR1'), help_text=_('[Trial 1] Percentage Coefficient - red'), null=True, blank=True)
    percentage_red_trial2 = FloatField(verbose_name=('PR2'), help_text=_('[Trial 2] Percentage Coefficient - red'), null=True, blank=True)
    percentage_white_trial1 = FloatField(verbose_name=('PW1'), help_text=_('[Trial 1] Percentage Coefficient - white'), null=True, blank=True)
    percentage_white_trial2 = FloatField(verbose_name=('PW2'), help_text=_('[Trial 2] Percentage Coefficient - white'), null=True, blank=True)

    # Time Coefficient Standard Deviation of 80% median intervals
    time_stdev_all_trial1 = FloatField(verbose_name=('TSD_1'), help_text=_('[Trial 1] Time Coefficient Standard Deviation - all'), null=True, blank=True)
    time_stdev_all_trial2 = FloatField(verbose_name=('TSD_2'), help_text=_('[Trial 2] Time Coefficient Standard Deviation - all'), null=True, blank=True)
    time_stdev_blue_trial1 = FloatField(verbose_name=('TSDB1'), help_text=_('[Trial 1] Time Coefficient Standard Deviation - blue'), null=True, blank=True)
    time_stdev_blue_trial2 = FloatField(verbose_name=('TSDB2'), help_text=_('[Trial 2] Time Coefficient Standard Deviation - blue'), null=True, blank=True)
    time_stdev_red_trial1 = FloatField(verbose_name=('TSDR1'), help_text=_('[Trial 1] Time Coefficient Standard Deviation - red'), null=True, blank=True)
    time_stdev_red_trial2 = FloatField(verbose_name=('TSDR2'), help_text=_('[Trial 2] Time Coefficient Standard Deviation - red'), null=True, blank=True)
    time_stdev_white_trial1 = FloatField(verbose_name=('TSDW1'), help_text=_('[Trial 1] Time Coefficient Standard Deviation - white'), null=True, blank=True)
    time_stdev_white_trial2 = FloatField(verbose_name=('TSDW2'), help_text=_('[Trial 2] Time Coefficient Standard Deviation - white'), null=True, blank=True)

    # Time Coefficient Mean of 80% median intervals
    time_mean_all_trial1 = FloatField(verbose_name=('TM_1'), help_text=_('[Trial 1] Time Coefficient Mean - all'), null=True, blank=True)
    time_mean_all_trial2 = FloatField(verbose_name=('TM_2'), help_text=_('[Trial 2] Time Coefficient Mean - all'), null=True, blank=True)
    time_mean_blue_trial1 = FloatField(verbose_name=('TMB1'), help_text=_('[Trial 1] Time Coefficient Mean - blue'), null=True, blank=True)
    time_mean_blue_trial2 = FloatField(verbose_name=('TMB2'), help_text=_('[Trial 2] Time Coefficient Mean - blue'), null=True, blank=True)
    time_mean_red_trial1 = FloatField(verbose_name=('TMR1'), help_text=_('[Trial 1] Time Coefficient Mean - red'), null=True, blank=True)
    time_mean_red_trial2 = FloatField(verbose_name=('TMR2'), help_text=_('[Trial 2] Time Coefficient Mean - red'), null=True, blank=True)
    time_mean_white_trial1 = FloatField(verbose_name=('TMW1'), help_text=_('[Trial 1] Time Coefficient Mean - white'), null=True, blank=True)
    time_mean_white_trial2 = FloatField(verbose_name=('TMW2'), help_text=_('[Trial 2] Time Coefficient Mean - white'), null=True, blank=True)

    def __str__(self):
        return f'{self.uid}'

    class Meta:
        ordering = ['-start_datetime']
        verbose_name = _('Experiment')
        verbose_name_plural = _('Experiments')


"""
    def calculate_results(self):
        #self.count_clicks_all()
        #out = self.count_clicks_valid()
        out = self.end - self.start
        print(out)

    def count_clicks_all(self):
        clicks = Event.objects.filter(trial=self, action='click')
        self.count_all = clicks.filter(target__in=['blue', 'red', 'white']).count()
        self.count_blue = clicks.filter(target='blue').count()
        self.count_red = clicks.filter(target='red').count()
        self.count_white = clicks.filter(target='white').count()
        self.save()

    def count_clicks_valid(self):
        clicks = Event.objects.filter(trial=self).order_by('datetime')
        return {
            'all': list(clicks.filter(target__in=['blue', 'red', 'white']))[5:-5],
            'blue': list(clicks.filter(target='blue'))[5:-5],
            'red': list(clicks.filter(target='red'))[5:-5],
            'white': list(clicks.filter(target='white'))[5:-5]}

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
"""
