import statistics

from django.db import models
from django.db.models import DateTimeField
from django.db.models import CharField
from django.db.models import FloatField
from django.db.models import ForeignKey
from django.db.models import EmailField
from django.db.models import NullBooleanField
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
    regularity = PositiveSmallIntegerField(verbose_name=_('Regularity'), help_text=_('Click every X seconds'))
    attempt = PositiveSmallIntegerField(verbose_name=_('Attempt'), db_index=True)
    is_valid = NullBooleanField(verbose_name=_('Is Valid?'), default=None, db_index=True)

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

    def save(self, *args, **kwargs):
        self.uid = self.uid.lower()
        return super().save(*args, **kwargs)

    def validate(self):
        self.invalidate_clicks('blue')
        self.invalidate_clicks('red')
        self.invalidate_clicks('white')
        self.check_if_valid()

    def calculate(self):
        self.calculate_counts()
        self.calculate_percentage()
        self.calculate_stdev()
        self.calculate_mean()

    def invalidate_clicks(self, color, drop_percent=0.20):
        """
        Zostawiamy tylko 80% wyników, tj. odrzucamy pierwsze 20%
        """
        drop_count = int(self.timeout / self.regularity * drop_percent)
        clicks = Click.objects.filter(trial=self, color=color).order_by('datetime')

        for invalid in clicks[:drop_count]:
            invalid.is_valid = False
            invalid.save()

        for valid in clicks[drop_count:]:
            valid.is_valid = False
            valid.save()

    def calculate_counts(self):
        clicks = Click.objects.filter(trial=self, is_valid=True)
        self.count_all = clicks.all().count()
        self.count_blue = clicks.filter(color='blue').count()
        self.count_red = clicks.filter(color='red').count()
        self.count_white = clicks.filter(color='white').count()
        self.save()

    def calculate_percentage(self, precision=2):
        """
        Zliczam ilość wszystkich kliknięć na każdym z kolorów i sumuję je
        1. Określam procentowy współczynnik regularności: (ilość czasu / co ile sekund miał klikać) - 100%; n kliknięć - x%
        2. Wyliczenie procentowych współczynników regularności (z kroku powyżej) dla każdego z kolorów osobno
        3. >>> {"biały": 100, "czerwony": 110, "niebieski": 90} // wartości są w procentach
        """
        percent_coefficient = self.timeout / self.regularity
        self.percentage_all = round(self.count_all / (percent_coefficient * 3) * 100, precision)
        self.percentage_blue = round(self.count_blue / percent_coefficient * 100, precision)
        self.percentage_red = round(self.count_red / percent_coefficient * 100, precision)
        self.percentage_white = round(self.count_white / percent_coefficient * 100, precision)
        self.save()

    def check_if_valid(self, min=25, max=200):
        if min <= self.percentage_all <= max:
            self.is_valid = True
        else:
            self.is_valid = False
        self.save()

    def get_time_regularity_series(self):
        """
        Obliczamy czasowy współczynnik regularności dla koloru
        1. Dla każdego kliknięcia w kolorze od czasu następnego (n+1) kliknięcia odejmuj czas poprzedniego (n) - interwały czasu pomiędzy kliknięciami
        2. >>> {"czerwony": [1.025, 0.987, 1.000, 1.01...], "biały": [1.025, 0.987, 1.000, 1.01...], "niebieski": [1.025, 0.987, 1.000, 1.01...], "wszystkie": [1.025, 0.987, 1.000, 1.01...]}
        """
        clicks = Click.objects.filter(trial=self, is_valid=True)

        def get_time_deltas(series):
            for i in range(1, len(series)):
                d1 = series[i-1].datetime
                d2 = series[i].datetime
                yield (d2 - d1).total_seconds()

        blue = list(get_time_deltas(clicks.filter(color='blue')))
        red = list(get_time_deltas(clicks.filter(color='red')))
        white = list(get_time_deltas(clicks.filter(color='white')))

        return {
            'all': blue + red + white,
            'blue': blue,
            'red': red,
            'white': white}

    def calculate_stdev(self, precision=2):
        """
        Wyliczamy odchylenie standardowe dla wszystkich razem (po appendowaniu list - 60 elem), oraz dla każdego koloru osobno (listy po 20 elementów)
        1. podnosimy każdy element listy do kwadratu
        2. sumujemy kwadraty
        3. pierwiastkujemy sumę
        4. dzielimy pierwiastek przez ilość elementów
        """
        clicks = self.get_time_regularity_series()

        def stdev(series):
            try:
                return round(statistics.stdev(series), precision)
            except statistics.StatisticsError:
                return None

        self.time_stdev_all = stdev(clicks['all'])
        self.time_stdev_blue = stdev(clicks['blue'])
        self.time_stdev_red = stdev(clicks['red'])
        self.time_stdev_white = stdev(clicks['white'])
        self.save()

    def calculate_mean(self, precision=2):
        """
        Obliczamy średnią czasu dla wszystkich oraz dla każdego z kolorów osobno
        """
        clicks = self.get_time_regularity_series()

        def mean(series):
            try:
                mean = round(statistics.mean(series), precision)
                return abs(mean)
            except statistics.StatisticsError:
                return None

        self.time_mean_all = mean(clicks['all'])
        self.time_mean_blue = mean(clicks['blue'])
        self.time_mean_red = mean(clicks['red'])
        self.time_mean_white = mean(clicks['white'])
        self.save()
