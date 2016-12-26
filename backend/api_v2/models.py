from django.db import models


class Experiment(models.Model):
    start = models.DateTimeField()
    end = models.DateTimeField()
    trial1 = models.ForeignKey(to='api_v2.Trial')
    trial2 = models.ForeignKey(to='api_v2.Trial')
    is_valid = models.BooleanField()


class Trial(models.Model):
    #experiment = models.ForeignKey(to='api_v2.Experiment', null=True, blank=True, db_index=True)
    location = models.CharField(max_length=50, db_index=True)
    polarization = models.CharField(max_length=50)
    device = models.CharField(max_length=50, null=True, blank=True)
    colors = models.CharField(max_length=50, null=True, blank=True)
    seconds = models.PositiveSmallIntegerField()
    trial = models.PositiveSmallIntegerField(db_index=True)

    participant_email = models.EmailField(db_index=True)
    participant_age = models.PositiveSmallIntegerField(null=True, blank=True)
    participant_condition = models.CharField(max_length=50, null=True, blank=True)
    participant_gender = models.CharField(max_length=50, null=True, blank=True)
    participant_rhythm = models.CharField(max_length=50, null=True, blank=True)

    def add(*args, **kwargs):
        survey = kwargs['survey']
        events = kwargs['events']
        del kwargs['survey']
        del kwargs['events']
        trial = kwargs
        return trial


class Event(models.Model):
    trial = models.ForeignKey(to='api_v2.Trial', null=True, blank=True, db_index=True)
    datetime = models.DateTimeField()
    target = models.CharField(max_length=50, db_index=True)
    action = models.CharField(max_length=50, db_index=True)
