from django.contrib import admin
from backend.api_v2.models import Event
from backend.api_v2.models import Survey
from backend.api_v2.models import Trial


class SurveyInline(admin.StackedInline):
    model = Survey
    extra = 0

class EventInline(admin.TabularInline):
    model = Event
    extra = 0


@admin.register(Trial)
class TrialAdmin(admin.ModelAdmin):
    list_display = ['uid', 'attempt', 'location', 'device', 'colors', 'timeout',  'regularity', 'start_datetime', 'end_datetime']
    list_display_links = ['uid']
    list_filter = ['polarization', 'attempt', 'timeout', 'regularity', 'colors', 'device', 'location']
    ordering = ['-start_datetime']
    inlines = [SurveyInline, EventInline]


@admin.register(Survey)
class SurveyAdmin(admin.ModelAdmin):
    list_display = ['datetime', 'email', 'age', 'condition', 'gender', 'rhythm', 'trial']
    list_display_links = ['datetime']
    list_filter = ['gender', 'condition', 'rhythm', 'age']
    ordering = ['-datetime']


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['datetime', 'target', 'action', 'trial']
    list_display_links = ['datetime']
    list_filter = ['target', 'action']
    ordering = ['-datetime']
