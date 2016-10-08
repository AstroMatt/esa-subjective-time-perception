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
    list_display = ['view_datetime', 'last_name', 'first_name', 'age', 'condition', 'rhythm']
    list_filter = ['location', 'device', 'polarization', 'condition', 'rhythm', 'age']
    search_fields = ['^last_name']
    inlines = [EventInline, ClickInline]

    def view_datetime(self, obj):
        return '{date:%Y-%m-%d %H:%M}'.format(**obj.__dict__)
