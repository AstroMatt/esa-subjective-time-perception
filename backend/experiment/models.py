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
    location = CharField(verbose_name=_('Location'), max_length=50, db_index=True)
    device = CharField(verbose_name=_('Device'), max_length=50)

    start_datetime = DateTimeField(verbose_name=_('Start datetime'), db_index=True, null=True, blank=True)
    end_datetime = DateTimeField(verbose_name=_('End datetime'), null=True, blank=True)

    def __str__(self):
        return f'{self.uid}'


    # Count click events
    count_all = PositiveSmallIntegerField(verbose_name=_('Count click events - all'), null=True, blank=True)
    count_blue = PositiveSmallIntegerField(verbose_name=_('Count click events - blue'), null=True, blank=True)
    count_red = PositiveSmallIntegerField(verbose_name=_('Count click events - red'), null=True, blank=True)
    count_white = PositiveSmallIntegerField(verbose_name=_('Count click events - white'), null=True, blank=True)

    # Percentage cefficient for 80% of median intervals
    percentage_all = FloatField(verbose_name=_('Percentage coefficient - all'), null=True, blank=True)
    percentage_blue = FloatField(verbose_name=_('Percentage coefficient - blue'), null=True, blank=True)
    percentage_red = FloatField(verbose_name=_('Percentage coefficient - red'), null=True, blank=True)
    percentage_white = FloatField(verbose_name=_('Percentage coefficient - white'), null=True, blank=True)

    # Time coefficient standard deviation of 80% median intervals
    time_stdev_all = FloatField(verbose_name=_('Time coefficient standard deviation - all'), null=True, blank=True)
    time_stdev_blue = FloatField(verbose_name=_('Time coefficient standard deviation - blue'), null=True, blank=True)
    time_stdev_red = FloatField(verbose_name=_('Time coefficient standard deviation - red'), null=True, blank=True)
    time_stdev_white = FloatField(verbose_name=_('Time coefficient standard deviation - white'), null=True, blank=True)

    # Time coefficient mean of 80% median intervals
    time_mean_all = FloatField(verbose_name=_('Time coefficient mean - all'), null=True, blank=True)
    time_mean_blue = FloatField(verbose_name=_('Time coefficient mean - blue'), null=True, blank=True)
    time_mean_red = FloatField(verbose_name=_('Time coefficient mean - red'), null=True, blank=True)
    time_mean_white = FloatField(verbose_name=_('Time coefficient mean - white'), null=True, blank=True)



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
