from django.utils.translation import ugettext_lazy as _
from django.db import models


class Experiment(models.Model):
    RHYTHMS = [
        ('perfect', _('Perfect')),
        ('above average', _('Above average')),
        ('average', _('Average')),
        ('below average', _('Below average')),
        ('poor', _('Poor'))]
    GENDERS = [
        ('female', _('Female')),
        ('male', _('Male')),
        ('other', _('Other'))]
    CONDITIONS = [
        ('well rested', _('Well rested')),
        ('normal', _('Normal')),
        ('tired', _('Tired'))]
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.PositiveSmallIntegerField()
    rhythm = models.CharField(max_length=50, choices=RHYTHMS)
    gender = models.CharField(max_length=50, choices=GENDERS)
    condition = models.CharField(max_length=50, choices=CONDITIONS)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return '[{start_date}] {last_name}, {first_name}'.format(**self.__dict__)

    class Meta:
        ordering = ["-start_date"]
        verbose_name = _("Experiment")
        verbose_name_plural = _("Experiments")


class Click(models.Model):
    BACKGROUNDS = [
        ('white', _('White')),
        ('blue', _('Blue')),
        ('red', _('Red'))]
    experiment = models.ForeignKey(to='experiment.Experiment')
    datetime = models.DateTimeField()
    background = models.CharField(max_length=15, choices=BACKGROUNDS)

    def __str__(self):
        return '{datetime} {background}'.format(**self.__dict__)

    class Meta:
        ordering = ["-datetime"]
        verbose_name = _("Click event")
        verbose_name_plural = _("Click events")
