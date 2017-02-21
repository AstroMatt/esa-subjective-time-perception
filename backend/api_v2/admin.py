from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from backend.api_v2.models import Click
from backend.api_v2.models import Event
from backend.api_v2.models import Survey
from backend.api_v2.models import Trial


class SurveyInline(admin.StackedInline):
    model = Survey
    extra = 0


class ClickInline(admin.TabularInline):
    model = Click
    extra = 0


class EventInline(admin.TabularInline):
    model = Event
    extra = 0


@admin.register(Trial)
class TrialAdmin(ImportExportModelAdmin):
    list_display = ['uid', 'attempt', 'location', 'device', 'colors', 'timeout',  'regularity', 'start_datetime', 'end_datetime']
    list_display_links = ['uid']
    list_filter = ['polarization', 'attempt', 'timeout', 'regularity', 'colors', 'device', 'location']
    search_fields = ['^uid']
    ordering = ['-start_datetime']
    #inlines = [SurveyInline, EventInline, ClickInline]


@admin.register(Survey)
class SurveyAdmin(ImportExportModelAdmin):
    list_display = ['datetime', 'email', 'age', 'condition', 'gender', 'rhythm', 'trial']
    list_display_links = ['datetime']
    list_filter = ['gender', 'condition', 'rhythm', 'age']
    search_fields = ['^email']
    ordering = ['-datetime']


@admin.register(Event)
class EventAdmin(ImportExportModelAdmin):
    list_display = ['datetime', 'target', 'action', 'trial']
    list_display_links = ['datetime']
    list_filter = ['target', 'action']
    search_fields = ['=trial__id']
    ordering = ['-datetime']


@admin.register(Click)
class ClickAdmin(ImportExportModelAdmin):
    list_display = ['datetime', 'is_valid', 'color']
    list_display_links = ['datetime']
    list_filter = ['is_valid', 'color']
    search_fields = ['=trial__id']
    ordering = ['-datetime']
