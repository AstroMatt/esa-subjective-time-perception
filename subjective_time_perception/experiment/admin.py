from django.contrib import admin
from subjective_time_perception.experiment.models import Experiment
from subjective_time_perception.experiment.models import Click
from subjective_time_perception.experiment.models import Event


class ClickInline(admin.TabularInline):
    model = Click
    extra = 0


class EventInline(admin.TabularInline):
    model = Event
    extra = 0


@admin.register(Experiment)
class ExperimentAdmin(admin.ModelAdmin):
    list_display = ['created', 'last_name', 'first_name', 'age', 'condition', 'rhythm']
    list_filter = ['age', 'condition', 'rhythm']
    search_fields = ['^last_name']
    inlines = [EventInline, ClickInline]
