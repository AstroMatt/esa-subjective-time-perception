from django.db import models


class Experiment(models.Model):
    start = models.DateTimeField()
    end = models.DateTimeField()
    trial1 = models.ForeignKey(to='api_v2.Trial', related_name='trial1')
    trial2 = models.ForeignKey(to='api_v2.Trial', related_name='trial2')
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
        survey = kwargs.get('survey')
        events = kwargs.get('events')
        trial = kwargs.get('configuration')

        with open('/developer/esa-act-subjective-time-perception/temp/api_v2-sample.json', 'w') as file:
            import json
            data = json.dumps(kwargs, sort_keys=True, indent=4)
            file.write(data)

        return trial


class Event(models.Model):
    trial = models.ForeignKey(to='api_v2.Trial', null=True, blank=True, db_index=True)
    datetime = models.DateTimeField()
    target = models.CharField(max_length=50, db_index=True)
    action = models.CharField(max_length=50, db_index=True)
