import json
import statistics
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class Click(models.Model):
    result = models.ForeignKey(verbose_name=_('Result'), to='api_v3.Result')
    datetime = models.DateTimeField(verbose_name=_('Datetime'))
    color = models.CharField(verbose_name=_('Target'), max_length=50)
    is_valid = models.NullBooleanField(verbose_name=_('Is Valid?'), default=None)

    class Meta:
        verbose_name = _('Click')
        verbose_name_plural = _('Click')

    def __str__(self):
        return f'[{self.datetime:%Y-%m-%d %H:%M:%S.%f}] {self.color}'


class Result(models.Model):
    TIME_AFTER_SLEEP = 'after-sleep'
    TIME_BEFORE_SLEEP = 'before-sleep'
    TIME_OTHER = 'other'
    TIME_CHOICES = [
        (TIME_AFTER_SLEEP, _('After Sleep')),
        (TIME_BEFORE_SLEEP, _('Before Sleep')),
        (TIME_OTHER, _('Other'))]

    GENDER_FEMALE = 'female'
    GENDER_MALE = 'male'
    GENDER_OTHER = 'other'
    GENDER_CHOICES = [
        (GENDER_FEMALE, _('Female')),
        (GENDER_MALE, _('Male')),
        (GENDER_OTHER, _('Other'))]

    CONDITION_RESTED = 'rested'
    CONDITION_NORMAL = 'normal'
    CONDITION_TIRED = 'tired'
    CONDITION_CHOICES = [
        (CONDITION_RESTED, _('Well rested')),
        (CONDITION_NORMAL, _('Normal')),
        (CONDITION_TIRED, _('Tired'))]

    STATUS_ADDED = 'added'
    STATUS_PARSED = 'parsed'
    STATUS_ERROR = 'error'
    STATUS_VALID = 'valid'
    STATUS_INVALID = 'invalid'
    STATUS_RECALCULATE = 'recalculate'
    STATUS_CHOICES = [
        (STATUS_ADDED, _('Added')),
        (STATUS_PARSED, _('Parsed')),
        (STATUS_ERROR, _('Error')),
        (STATUS_VALID, _('Valid')),
        (STATUS_INVALID, _('Invalid')),
        (STATUS_RECALCULATE, _('To Recalculate'))]

    # request_data = models.TextField(verbose_name=_('HTTP Request JSON'), null=True, blank=True, default=None)
    request_sha1 = models.CharField(verbose_name=_('HTTP Request SHA1'), max_length=40, db_index=True, unique=True)
    status = models.CharField(verbose_name=_('Status'), max_length=30, choices=STATUS_CHOICES, default=STATUS_ADDED)

    start_datetime = models.DateTimeField(verbose_name=_('Start datetime'))
    end_datetime = models.DateTimeField(verbose_name=_('End datetime'), db_index=True)
    colors = models.CharField(verbose_name=_('Color order'), max_length=50)
    device = models.CharField(verbose_name=_('Device'), max_length=50)
    location = models.CharField(verbose_name=_('Location'), max_length=50)
    email = models.EmailField(verbose_name=_('User Email'), db_index=True)
    timeout = models.FloatField(verbose_name=_('Timeout'), help_text=_('Seconds per color'))
    regularity = models.PositiveSmallIntegerField(verbose_name=_('Regularity'), help_text=_('Click every X seconds'))
    time_between_clicks = models.TextField(verbose_name=_('Time between clicks'), blank=True, null=True, default=None)
    results = models.NullBooleanField(verbose_name=_('Results was shown?'), blank=True, null=True, default=None)

    # TODO: clicks_expected
    # TODO: clicks_minimum
    # TODO: click_maximum

    survey_age = models.PositiveSmallIntegerField(verbose_name=_('Age'))
    survey_condition = models.CharField(verbose_name=_('Condition'), max_length=50, choices=CONDITION_CHOICES)
    survey_gender = models.CharField(verbose_name=_('Gender'), max_length=50, choices=GENDER_CHOICES)
    survey_time = models.CharField(verbose_name=_('Time'), max_length=50, choices=TIME_CHOICES)
    survey_temperature = models.DecimalField(verbose_name=_('Temperature'), help_text=_('Celsius'), max_digits=3, decimal_places=1, null=True, blank=True, default=None)
    survey_bp_systolic = models.PositiveSmallIntegerField(verbose_name=_('Blood Pressure SYS'), null=True, blank=True, default=None)
    survey_bp_diastolic = models.PositiveSmallIntegerField(verbose_name=_('Blood Pressure DIA'), null=True, blank=True, default=None)
    survey_heart_rate = models.PositiveSmallIntegerField(verbose_name=_('Heart Rate'), help_text=_('bpm'), null=True, blank=True, default=None)

    count_all = models.PositiveSmallIntegerField(verbose_name=_('Count'), null=True, blank=True)
    count_blue = models.PositiveSmallIntegerField(verbose_name=_('Count - blue'), null=True, blank=True)
    count_red = models.PositiveSmallIntegerField(verbose_name=_('Count - red'), null=True, blank=True)
    count_white = models.PositiveSmallIntegerField(verbose_name=_('Count - white'), null=True, blank=True)

    tempo_all = models.FloatField(verbose_name=_('Tempo'), null=True, blank=True)
    tempo_blue = models.FloatField(verbose_name=_('Tempo - blue'), null=True, blank=True)
    tempo_red = models.FloatField(verbose_name=_('Tempo - red'), null=True, blank=True)
    tempo_white = models.FloatField(verbose_name=_('Tempo - white'), null=True, blank=True)

    regularity_all = models.FloatField(verbose_name=_('Regularity'), null=True, blank=True)
    regularity_blue = models.FloatField(verbose_name=_('Regularity - blue'), null=True, blank=True)
    regularity_red = models.FloatField(verbose_name=_('Regularity - red'), null=True, blank=True)
    regularity_white = models.FloatField(verbose_name=_('Regularity - white'), null=True, blank=True)

    interval_all = models.FloatField(verbose_name=_('Interval'), null=True, blank=True)
    interval_blue = models.FloatField(verbose_name=_('Interval - blue'), null=True, blank=True)
    interval_red = models.FloatField(verbose_name=_('Interval - red'), null=True, blank=True)
    interval_white = models.FloatField(verbose_name=_('Interval - white'), null=True, blank=True)

    def get_absolute_url(self):
        return reverse('api-v3:report', args=[self.uid])

    @staticmethod
    def add(request_sha1, result, clicks):
        try:
            # TODO: Remove this temporary fix
            if 'survey_sleep' in result.keys():
                del result['survey_sleep']

            result, _ = Result.objects.get_or_create(request_sha1=request_sha1, defaults=result)

            for click in clicks:
                Click.objects.get_or_create(result=result, **click)

            result.validate()
            result.calculate()

            Click.objects.filter(result=result).delete()
            return result

        except Exception as message:
            from backend.logger.models import HTTPRequest
            http_request = HTTPRequest.objects.get(sha1=request_sha1)
            http_request.error(message)

    def __str__(self):
        return f'({self.request_sha1:.7}) [{self.start_datetime:%Y-%m-%d %H:%M}] {self.email}'

    class Meta:
        verbose_name = _('Result')
        verbose_name_plural = _('Results')

    def get_data(self):
        data = self.__dict__.copy()
        data.pop('_state')
        return data

    def save(self, *args, **kwargs):
        self.email = self.email.lower()
        return super().save(*args, **kwargs)

    def validate(self):
        self.validate_clicks('blue')
        self.validate_clicks('red')
        self.validate_clicks('white')
        self.validate_result()

    def calculate(self):
        self.calculate_count()
        self.calculate_tempo()
        self.calculate_regularity()
        self.calculate_interval()

    def validate_clicks(self, color, elements_to_drop=2):
        clicks = Click.objects.filter(result=self, color=color).order_by('datetime')

        for invalid in clicks[:elements_to_drop]:
            invalid.is_valid = False
            invalid.save()

        for valid in clicks[elements_to_drop:]:
            valid.is_valid = True
            valid.save()

    def validate_result(self, min=25, max=200):
        if not self.tempo_all:
            self.calculate()

        if min <= self.tempo_all <= max:
            self.status = self.STATUS_VALID
        else:
            self.status = self.STATUS_INVALID
        self.save()

    def get_time_between_clicks(self):
        """
        Obliczamy czasowy współczynnik regularności dla koloru
        1. Dla każdego kliknięcia w kolorze od czasu następnego (n+1) kliknięcia odejmuj czas poprzedniego (n) - interwały czasu pomiędzy kliknięciami
        2. >>> {"czerwony": [1.025, 0.987, 1.000, 1.01...], "biały": [1.025, 0.987, 1.000, 1.01...], "niebieski": [1.025, 0.987, 1.000, 1.01...], "wszystkie": [1.025, 0.987, 1.000, 1.01...]}
        """
        clicks = Click.objects.filter(result=self, is_valid=True).order_by('datetime')

        def get_time_deltas(series):
            for i in range(1, len(series)):
                d1 = series[i - 1].datetime
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
        clicks = Click.objects.filter(result=self, is_valid=True)
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
