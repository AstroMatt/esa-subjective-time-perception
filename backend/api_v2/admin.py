from django.contrib import admin
from backend.api_v2.models import Event
from backend.api_v2.models import Survey
from backend.api_v2.models import Trial


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    pass


@admin.register(Trial)
class TrialAdmin(admin.ModelAdmin):
    pass


@admin.register(Survey)
class SurveyAdmin(admin.ModelAdmin):
    pass
