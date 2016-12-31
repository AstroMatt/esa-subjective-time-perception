from django.contrib import admin
from backend.experiment.models import Experiment


@admin.register(Experiment)
class ExperimentAdmin(admin.ModelAdmin):
    list_filter = ['is_valid', 'device', 'location']
    list_display = ['is_valid', 'uid', 'device', 'location', 'start', 'end']
    list_display_links = ['uid']
