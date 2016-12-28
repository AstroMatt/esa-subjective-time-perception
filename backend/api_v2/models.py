from django.db import models


class Experiment(models.Model):
    """
    {
        'ID': experiment.id,
        'name': '{last_name} {first_name}'.format(**experiment.__dict__),
        'polarization': experiment.polarization,
        'start_date': experiment.experiment_start,

        'C1': experiment.count_clicks()['all'],
        'CW1': experiment.count_clicks()['white'],
        'CR1': experiment.count_clicks()['red'],
        'CB1': experiment.count_clicks()['blue'],

        'PC1': experiment.regularity_coefficient_percent()['all'],
        'PCW1': experiment.regularity_coefficient_percent()['white'],
        'PCR1': experiment.regularity_coefficient_percent()['red'],
        'PCB1': experiment.regularity_coefficient_percent()['blue'],

        'TCSD1': experiment.stdev()['all'],
        'TCSDW1': experiment.stdev()['white'],
        'TCSDR1': experiment.stdev()['red'],
        'TCSDB1': experiment.stdev()['blue'],

        'TCM1': experiment.mean()['all'],
        'TCMW1': experiment.mean()['white'],
        'TCMR1': experiment.mean()['red'],
        'TCMB1': experiment.mean()['blue'],
    }
    """

    #trial1 = models.OneToOneField(to='api_v2.Trial', related_name='trial1')
    #trial2 = models.OneToOneField(to='api_v2.Trial', related_name='trial2')
    #survey = models.OneToOneField(to='api_v2.Survey')
    is_valid = models.NullBooleanField()
    tcmb1 = models.FloadField(
        verbose_name=_(),
        help=_(),
    )


class Trial(models.Model):
    #experiment = models.ForeignKey(to='api_v2.Experiment', null=True, blank=True, db_index=True)

    start = models.DateTimeField()
    end = models.DateTimeField()
    colors = models.CharField(max_length=50, null=True, blank=True)
    device = models.CharField(max_length=50, null=True, blank=True)
    location = models.CharField(max_length=50, db_index=True)
    participant = models.EmailField(db_index=True)
    polarization = models.CharField(max_length=50)
    seconds = models.PositiveSmallIntegerField()
    trial = models.PositiveSmallIntegerField(db_index=True)

    def add(*args, **kwargs):
        survey = kwargs.get('survey')
        events = kwargs.get('events')
        trial = kwargs.get('configuration')


class Survey(models.Model):
    #experiment = models.ForeignKey(to='api_v2.Experiment', null=True, blank=True, db_index=True)
    trial = models.ForeignKey(to='api_v2.Trial', null=True, blank=True, db_index=True)

    age = models.PositiveSmallIntegerField(null=True, blank=True)
    condition = models.CharField(max_length=50, null=True, blank=True)
    gender = models.CharField(max_length=50, null=True, blank=True)
    rhythm = models.CharField(max_length=50, null=True, blank=True)


class Event(models.Model):
    trial = models.ForeignKey(to='api_v2.Trial', null=True, blank=True, db_index=True)

    datetime = models.DateTimeField()
    target = models.CharField(max_length=50, db_index=True)
    action = models.CharField(max_length=50, db_index=True)
