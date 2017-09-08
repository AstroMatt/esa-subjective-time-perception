import json
import statistics

from django.db import models
from django.db.models import DateTimeField
from django.db.models import CharField
from django.db.models import FloatField
from django.db.models import EmailField
from django.db.models import NullBooleanField
from django.db.models import PositiveSmallIntegerField
from django.db.models import TextField
from django.utils.translation import ugettext_lazy as _

from backend.api_v2.models import Click


class Trial(models.Model):
    TIME_MORNING = 'morning'
    TIME_EVENING = 'evening'
    TIME_OTHER = 'other'

    TIME_CHOICES = [
        (TIME_MORNING, _('Morning')),
        (TIME_EVENING, _('Evening')),
        (TIME_OTHER, _('Other')),
    ]

    start_datetime = DateTimeField(verbose_name=_('Start datetime'), db_index=True)
    end_datetime = DateTimeField(verbose_name=_('End datetime'))
    colors = CharField(verbose_name=_('Color order'), max_length=50)
    device = CharField(verbose_name=_('Device'), max_length=50)
    location = CharField(verbose_name=_('Location'), max_length=50)
    time = CharField(verbose_name=_('Time'), max_length=30, choices=TIME_CHOICES, null=True, blank=True, default=None)
    uid = EmailField(verbose_name=_('User ID'), db_index=True)
    polarization = CharField(verbose_name=_('Polarization'), max_length=50, null=True, blank=True, default=None)
    timeout = FloatField(verbose_name=_('Timeout'), help_text=_('Seconds per color'))
    regularity = PositiveSmallIntegerField(verbose_name=_('Regularity'), help_text=_('Click every X seconds'))
    attempt = PositiveSmallIntegerField(verbose_name=_('Attempt'), null=True, blank=True, default=True)
    is_valid = NullBooleanField(verbose_name=_('Is Valid?'), default=None, db_index=True)
    time_between_clicks = TextField(verbose_name=_('Time between clicks'), blank=True, null=True, default=None)

    count_all = PositiveSmallIntegerField(verbose_name=_('Count'), null=True, blank=True)
    count_blue = PositiveSmallIntegerField(verbose_name=_('Count - blue'), null=True, blank=True)
    count_red = PositiveSmallIntegerField(verbose_name=_('Count - red'), null=True, blank=True)
    count_white = PositiveSmallIntegerField(verbose_name=_('Count - white'), null=True, blank=True)

    tempo_all = FloatField(verbose_name=_('Tempo'), null=True, blank=True)
    tempo_blue = FloatField(verbose_name=_('Tempo - blue'), null=True, blank=True)
    tempo_red = FloatField(verbose_name=_('Tempo - red'), null=True, blank=True)
    tempo_white = FloatField(verbose_name=_('Tempo - white'), null=True, blank=True)

    regularity_all = FloatField(verbose_name=_('Regularity'), null=True, blank=True)
    regularity_blue = FloatField(verbose_name=_('Regularity - blue'), null=True, blank=True)
    regularity_red = FloatField(verbose_name=_('Regularity - red'), null=True, blank=True)
    regularity_white = FloatField(verbose_name=_('Regularity - white'), null=True, blank=True)

    interval_all = FloatField(verbose_name=_('Interval'), null=True, blank=True)
    interval_blue = FloatField(verbose_name=_('Interval - blue'), null=True, blank=True)
    interval_red = FloatField(verbose_name=_('Interval - red'), null=True, blank=True)
    interval_white = FloatField(verbose_name=_('Interval - white'), null=True, blank=True)

    def __str__(self):
        return f'[{self.start_datetime:%Y-%m-%d %H:%M}] ({self.location}, {self.device}) {self.uid}'

    class Meta:
        verbose_name = _('Trial')
        verbose_name_plural = _('Trials')

    def get_data(self):
        data = self.__dict__.copy()
        data.pop('_state')
        return data

    def save(self, *args, **kwargs):
        self.uid = self.uid.lower()
        return super().save(*args, **kwargs)

    def validate(self):
        self.validate_clicks('blue')
        self.validate_clicks('red')
        self.validate_clicks('white')
        self.validate_trial()

    def calculate(self):
        self.calculate_count()
        self.calculate_tempo()
        self.calculate_regularity()
        self.calculate_interval()

    def validate_clicks(self, color, elements_to_drop=2):
        clicks = Click.objects.filter(trial=self, color=color).order_by('datetime')

        for invalid in clicks[:elements_to_drop]:
            invalid.is_valid = False
            invalid.save()

        for valid in clicks[elements_to_drop:]:
            valid.is_valid = True
            valid.save()

    def validate_trial(self, min=25, max=200):
        if not self.tempo_all:
            self.calculate()

        if min <= self.tempo_all <= max:
            self.is_valid = True
        else:
            self.is_valid = False
        self.save()

    def get_time_between_clicks(self):
        """
        Obliczamy czasowy współczynnik regularności dla koloru
        1. Dla każdego kliknięcia w kolorze od czasu następnego (n+1) kliknięcia odejmuj czas poprzedniego (n) - interwały czasu pomiędzy kliknięciami
        2. >>> {"czerwony": [1.025, 0.987, 1.000, 1.01...], "biały": [1.025, 0.987, 1.000, 1.01...], "niebieski": [1.025, 0.987, 1.000, 1.01...], "wszystkie": [1.025, 0.987, 1.000, 1.01...]}
        """
        clicks = Click.objects.filter(trial=self, is_valid=True).order_by('datetime')

        def get_time_deltas(series):
            for i in range(1, len(series)):
                d1 = series[i-1].datetime
                d2 = series[i].datetime
                yield (d2 - d1).total_seconds()

        blue = list(get_time_deltas(clicks.filter(color='blue')))
        red = list(get_time_deltas(clicks.filter(color='red')))
        white = list(get_time_deltas(clicks.filter(color='white')))

        time_regularity_series = {
            'all': blue + red + white,
            'blue': blue,
            'red': red,
            'white': white}

        self.time_between_clicks = json.dumps(time_regularity_series)
        self.save()

        return time_regularity_series

    def calculate_count(self):
        clicks = Click.objects.filter(trial=self, is_valid=True)
        self.count_all = clicks.all().count()
        self.count_blue = clicks.filter(color='blue').count()
        self.count_red = clicks.filter(color='red').count()
        self.count_white = clicks.filter(color='white').count()
        self.save()

    def calculate_tempo(self, precision=2):
        """
        Zliczam ilość wszystkich kliknięć na każdym z kolorów i sumuję je
        1. Określam procentowy współczynnik regularności: (ilość czasu / co ile sekund miał klikać) - 100%; n kliknięć - x%
        2. Wyliczenie procentowych współczynników regularności (z kroku powyżej) dla każdego z kolorów osobno
        3. >>> {"biały": 100, "czerwony": 110, "niebieski": 90} // wartości są w procentach
        """
        percent_coefficient = float(self.timeout) / float(self.regularity)
        self.tempo_all = round(self.count_all / (percent_coefficient * 3) * 100, precision)
        self.tempo_blue = round(self.count_blue / percent_coefficient * 100, precision)
        self.tempo_red = round(self.count_red / percent_coefficient * 100, precision)
        self.tempo_white = round(self.count_white / percent_coefficient * 100, precision)
        self.save()

    def calculate_regularity(self, precision=4):
        """
        Wyliczamy odchylenie standardowe dla wszystkich razem (po appendowaniu list - 60 elem), oraz dla każdego koloru osobno (listy po 20 elementów)
        1. podnosimy każdy element listy do kwadratu
        2. sumujemy kwadraty
        3. pierwiastkujemy sumę
        4. dzielimy pierwiastek przez ilość elementów
        """
        clicks = self.get_time_between_clicks()

        def stdev(series):
            try:
                return round(statistics.stdev(series), precision)
            except statistics.StatisticsError:
                return None

        self.regularity_all = stdev(clicks['all'])
        self.regularity_blue = stdev(clicks['blue'])
        self.regularity_red = stdev(clicks['red'])
        self.regularity_white = stdev(clicks['white'])
        self.save()

    def calculate_interval(self, precision=4):
        clicks = self.get_time_between_clicks()

        def mean(series):
            try:
                mean = round(statistics.mean(series), precision)
                return abs(mean)
            except statistics.StatisticsError:
                return None

        self.interval_all = mean(clicks['all'])
        self.interval_blue = mean(clicks['blue'])
        self.interval_red = mean(clicks['red'])
        self.interval_white = mean(clicks['white'])
        self.save()
