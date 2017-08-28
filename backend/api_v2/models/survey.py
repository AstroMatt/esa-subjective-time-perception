from django.db import models
from django.db.models import DateTimeField
from django.db.models import DecimalField
from django.db.models import CharField
from django.db.models import ForeignKey
from django.db.models import EmailField
from django.db.models import PositiveSmallIntegerField
from django.utils.translation import ugettext_lazy as _


class Survey(models.Model):
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

    trial = ForeignKey(verbose_name=_('Trial'), to='api_v2.Trial', db_index=True)
    datetime = DateTimeField(verbose_name=_('Datetime'), db_index=True)
    email = EmailField(verbose_name=_('Email'), db_index=True)
    age = PositiveSmallIntegerField(verbose_name=_('Age'))
    condition = CharField(verbose_name=_('Condition'), max_length=50, choices=CONDITION_CHOICES)
    gender = CharField(verbose_name=_('Gender'), max_length=50, choices=GENDER_CHOICES)
    rhythm = CharField(verbose_name=_('Rhythm'), max_length=50, null=True, blank=True, default=None, editable=False)

    temperature = DecimalField(verbose_name=_('Temperature'), help_text=_('Celsius'), max_digits=3, decimal_places=1, null=True, blank=True, default=None)
    bp_systolic = PositiveSmallIntegerField(verbose_name=_('Blood Pressure SYS'), null=True, blank=True, default=None)
    bp_diastolic = PositiveSmallIntegerField(verbose_name=_('Blood Pressure DIA'), null=True, blank=True, default=None)
    heart_rate = PositiveSmallIntegerField(verbose_name=_('Heart Rate'), help_text=_('bpm'), null=True, blank=True, default=None)
    sleep_hours = PositiveSmallIntegerField(verbose_name=_('Sleep Hours'), null=True, blank=True, default=None)
    sleep_minutes = PositiveSmallIntegerField(verbose_name=_('Sleep Minutes'), null=True, blank=True, default=None)

    def __str__(self):
        return f'{self.datetime}'

    class Meta:
        verbose_name = _('Survey')
        verbose_name_plural = _('Surveys')
