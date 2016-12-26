from django.db import models


class Experiment(models.Model):
    start = models.DateTimeField()
    email = models.EmailField()
    is_valid = models.BooleanField()


class Trial(models.Model):
    experiment = models.ForeignKey(to='api_v2.Experiment')
    location = models.CharField(max_length=50)
    polarization = models.CharField(max_length=50)
    device = models.CharField(max_length=50)
    colors = models.CharField(max_length=50)
    seconds = models.PositiveSmallIntegerField()
    trial = models.PositiveSmallIntegerField()


class Survey(models.Model)
    trial = models.ForeignKey(to='api_v2.Trial')
    age = models.PositiveSmallIntegerField()
    email = models.EmailField()
    condition = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    rhythm = models.CharField(max_length=50)


class Event(models.Model):
    trial = models.ForeignKey(to='api_v2.Trial')
    datetime = models.DateTimeField()
    target = models.CharField(max_length=50)
    action = models.CharField(max_length=50)
