from django.contrib import admin
from subjective_time_perception.experiment.models import Experiment
from subjective_time_perception.experiment.models import Click


class ClickInline(admin.TabularInline):
    model = Click
    extra = 0


@admin.register(Experiment)
class ExperimentAdmin(admin.ModelAdmin):
    list_display = ['start_date', 'end_date', 'last_name', 'first_name', 'age', 'condition', 'rhythm']
    list_filter = ['age', 'condition', 'rhythm']
    search_fields = ['^last_name']
    inlines = [ClickInline]
