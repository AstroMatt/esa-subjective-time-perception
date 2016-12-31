from django.db import models
from django.db.models import CharField
from django.db.models import DateTimeField
from django.db.models import EmailField
from django.db.models import FloatField
from django.db.models import ForeignKey
from django.db.models import PositiveSmallIntegerField
from django.utils.translation import ugettext_lazy as _


class Trial(models.Model):
    start = DateTimeField(db_index=True)
    end = DateTimeField()
    colors = CharField(max_length=50)
    device = CharField(max_length=50)
    location = CharField(max_length=50, db_index=True)
    uid = EmailField(db_index=True)
    polarization = CharField(max_length=50)
    seconds = PositiveSmallIntegerField()
    trial = PositiveSmallIntegerField(db_index=True)

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

    def __str__(self):
        #return f'[{self.start:%Y-%m-%d %H:%M}] {self.location} trial: {self.trial} ({self.device}, {self.polarization}) {self.uid}'
        return f'{self.start}'

    def calculate_results(self):
        print('Calculating results:', self)
