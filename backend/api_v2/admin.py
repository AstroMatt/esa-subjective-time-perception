from django.contrib import admin
from backend.api_v2.models import Event
from backend.api_v2.models import Survey
from backend.api_v2.models import Trial



@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['datetime', 'target', 'action', 'trial']
    list_display_links = ['datetime']
    list_filter = ['target', 'action']


@admin.register(Trial)
class TrialAdmin(admin.ModelAdmin):
    list_display = ['uid', 'trial', 'location', 'device', 'colors', 'seconds', 'start', 'end']
    list_display_links = ['uid']
    list_filter = ['polarization', 'trial', 'seconds', 'colors', 'device', 'location']
    ordering = ['uid', 'trial']


@admin.register(Survey)
class SurveyAdmin(admin.ModelAdmin):
    list_display = ['datetime', 'email', 'age', 'condition', 'gender', 'rhythm', 'trial']
    list_display_links = ['datetime']
    list_filter = ['gender', 'condition', 'rhythm', 'age']
