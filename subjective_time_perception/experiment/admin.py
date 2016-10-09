from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from subjective_time_perception.experiment.models import Experiment
from subjective_time_perception.experiment.models import Click
from subjective_time_perception.experiment.models import Event


@admin.register(Click)
class ClickAdmin(ImportExportModelAdmin):
    list_display = ['experiment', 'datetime', 'background']
    list_filter = ['background']

    def get_readonly_fields(self, request, obj=None):
        if obj:
            self.readonly_fields = [field.name for field in obj.__class__._meta.fields if field.name != 'id']
        return self.readonly_fields


@admin.register(Event)
class EventAdmin(ImportExportModelAdmin):
    list_display = ['experiment', 'datetime', 'action', 'message']
    list_filter = ['action', 'message']

    def get_readonly_fields(self, request, obj=None):
        if obj:
            self.readonly_fields = [field.name for field in obj.__class__._meta.fields if field.name != 'id']
        return self.readonly_fields


class ClickInline(admin.TabularInline):
    model = Click
    readonly_fields = ['datetime', 'background']
    extra = 0

    def has_delete_permission(self, request, obj=None):
        return False


class EventInline(admin.TabularInline):
    model = Event
    readonly_fields = ['datetime', 'message', 'action']
    extra = 0

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Experiment)
class ExperimentAdmin(ImportExportModelAdmin):
    list_display = ['when', 'last_name', 'first_name', 'age', 'device', 'polarization', 'order', 'is_valid']
    list_filter = ['is_valid', 'location', 'device', 'polarization', 'timeout', 'order', 'condition', 'rhythm', 'age']
    search_fields = ['^last_name']
    inlines = [ClickInline]
    fieldsets = [
        ('Experiment', {'fields': ['location', 'device', 'polarization', 'order', 'timeout', 'is_valid']}),
        ('Survey', {'fields': ['last_name', 'first_name', 'age', 'rhythm', 'condition']}),
        ('Dates', {'fields': ['experiment_start', 'experiment_end', 'white_start', 'white_end', 'blue_start', 'blue_end', 'red_start', 'red_end']}),
    ]

    def when(self, obj):
        return '{experiment_start:%Y-%m-%d %H:%M}'.format(**obj.__dict__)

    def get_readonly_fields(self, request, obj=None):
        if obj:
            self.readonly_fields = [field.name for field in obj.__class__._meta.fields if field.name != 'id']
        return self.readonly_fields
