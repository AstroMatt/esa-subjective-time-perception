from django.contrib import admin
from backend.api_v1.models import Experiment
from backend.api_v1.models import Trial
from backend.api_v1.models import Click
from backend.api_v1.models import Event


class ReadOnlyMixin:
    def get_readonly_fields(self, request, obj=None):
        if obj:
            self.readonly_fields = [field.name for field in obj.__class__._meta.fields if field.name != 'id']
        return self.readonly_fields


@admin.register(Click)
class ClickAdmin(ReadOnlyMixin, admin.ModelAdmin):
    list_display = ['experiment', 'datetime', 'background']
    list_filter = ['background']
    ordering = ['-datetime']


@admin.register(Trial)
class TrialAdmin(ReadOnlyMixin, admin.ModelAdmin):
    list_display = ['experiment', 'start', 'end', 'is_valid']
    list_filter = ['is_valid', 'device', 'polarization', 'order']
    ordering = ['-start']


@admin.register(Event)
class EventAdmin(ReadOnlyMixin, admin.ModelAdmin):
    list_display = ['experiment', 'datetime', 'action', 'message']
    list_filter = ['action', 'message']
    ordering = ['-datetime']


class TrialInline(admin.StackedInline):
    model = Trial
    extra = 1
    readonly_fields = ['polarization', 'device', 'order', 'start', 'end', 'white_start', 'white_end', 'blue_start', 'blue_end', 'red_start', 'red_end']

    def has_delete_permission(self, request, obj=None):
        return False

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
class ExperimentAdmin(ReadOnlyMixin, admin.ModelAdmin):
    list_display = ['when', 'last_name', 'first_name', 'age', 'device', 'polarization', 'order', 'is_valid']
    list_filter = ['is_valid', 'location', 'device', 'polarization', 'timeout', 'order', 'condition', 'rhythm', 'age']
    ordering = ['-experiment_start']
    search_fields = ['^last_name']
    inlines = [TrialInline, ClickInline]
    fieldsets = [
        ('Experiment', {'fields': ['location', 'device', 'polarization', 'order', 'timeout', 'is_valid']}),
        ('Survey', {'fields': ['last_name', 'first_name', 'age', 'rhythm', 'condition']}),
        ('Dates', {'fields': ['experiment_start', 'experiment_end', 'white_start', 'white_end', 'blue_start', 'blue_end', 'red_start', 'red_end']}),
    ]

    def when(self, obj):
        return '{experiment_start:%Y-%m-%d %H:%M}'.format(**obj.__dict__)
