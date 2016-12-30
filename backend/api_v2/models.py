from django.db import models


class Experiment(models.Model):
    #trial1 = models.OneToOneField(to='api_v2.Trial', related_name='trial1')
    #trial2 = models.OneToOneField(to='api_v2.Trial', related_name='trial2')
    #survey = models.OneToOneField(to='api_v2.Survey')
    is_valid = models.NullBooleanField()



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

    # Count click events
    count_all = models.PositiveSmallIntegerField(verbose_nam=_('Count click events - all'))
    count_white = models.PositiveSmallIntegerField(verbose_nam=_('Count click events - white'))
    count_red = models.PositiveSmallIntegerField(verbose_nam=_('Count click events - red'))
    count_blue = models.PositiveSmallIntegerField(verbose_nam=_('Count click events - blue'))

    # Percentage cefficient for 80% of inner intervals
    percentage_all = models.FloatField(verbose_name=_('Percentage coefficient - all'))
    percentage_white = models.FloatField(verbose_name=_('Percentage coefficient - white'))
    percentage_red = models.FloatField(verbose_name=_('Percentage coefficient - red'))
    percentage_blue = models.FloatField(verbose_name=_('Percentage coefficient - blue'))

    # Time coefficient standard deviation of 80% median intervals
    time_stdev_all = models.FloatField(verbose_name=_('Time coefficient standard deviation - all'))
    time_stdev_white = models.FloatField(verbose_name=_('Time coefficient standard deviation - white'))
    time_stdev_red = models.FloatField(verbose_name=_('Time coefficient standard deviation - red'))
    time_stdev_blue = models.FloatField(verbose_name=_('Time coefficient standard deviation - blue'))

    # Time coefficient mean of 80% median intervals
    time_mean_all = models.FloatField(verbose_name=_('Time coefficient mean - all'))
    time_mean_white = models.FloatField(verbose_name=_('Time coefficient mean - white'))
    time_mean_red = models.FloatField(verbose_name=_('Time coefficient mean - red'))
    time_mean_blue = models.FloatField(verbose_name=_('Time coefficient mean - blue'))

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
