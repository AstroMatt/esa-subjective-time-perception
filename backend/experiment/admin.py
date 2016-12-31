from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from backend.experiment.models import Experiment


admin.site.unregister(User)
admin.site.unregister(Group)


@admin.register(Experiment)
class ExperimentAdmin(admin.ModelAdmin):
    list_filter = ['is_valid', 'device', 'location']
    list_display = ['is_valid', 'uid', 'device', 'location', 'start_datetime', 'end_datetime']
    list_display_links = ['uid']
