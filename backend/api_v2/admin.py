from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from import_export.admin import ImportExportModelAdmin
from backend.api_v2.models import Click
from backend.api_v2.models import Event
from backend.api_v2.models import Survey
from backend.api_v2.models import Trial


class PercentageListFilter(admin.SimpleListFilter):
    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = _('Percentage all')

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'percentage_all'

    def lookups(self, request, model_admin):
        return [
            ('too-many', _('Invalid: more than 201%')),
            ('fast', _('Fast: 126% - 200%')),
            ('normal', _('Normal: 75% - 125%')),
            ('slow', _('Slow: 25% - 74%')),
            ('too-few', _('Invalid: less than 25%')),
        ]

    def queryset(self, request, queryset):
        if self.value() == 'too-many':
            return queryset.filter(percentage_all__gt=200)

        if self.value() == 'fast':
            return queryset.filter(percentage_all__gt=125, percentage_all__lte=200)

        if self.value() == 'normal':
            return queryset.filter(percentage_all__gte=75, percentage_all__lte=125)

        if self.value() == 'slow':
            return queryset.filter(percentage_all__gte=25, percentage_all__lt=75)

        if self.value() == 'too-few':
            return queryset.filter(percentage_all__lt=25)


class ValidateAction:
    def make_invalid(modeladmin, request, queryset):
        queryset.update(is_valid=False)
    make_invalid.short_description = _('Mark as invalid')

    def make_valid(modeladmin, request, queryset):
        queryset.update(is_valid=True)
    make_valid.short_description = _('Mark as valid')


class RecalculateAction:
    def recalculate(modeladmin, request, queryset):
        for trial in queryset:
            trial.calculate()
    recalculate.short_description = _('Recalculate')


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
class TrialAdmin(ImportExportModelAdmin, ValidateAction, RecalculateAction):
    list_display = ['is_valid', 'uid', 'end_datetime', 'timeout',  'regularity', 'count_all', 'percentage_all', 'time_stdev_all']
    list_display_links = ['uid']
    list_filter = [PercentageListFilter, 'is_valid', 'polarization', 'attempt', 'timeout', 'regularity', 'colors', 'device', 'location']
    search_fields = ['=id', '^uid']
    ordering = ['-start_datetime']
    actions = ['make_invalid', 'make_valid', 'recalculate']
    inlines = [SurveyInline, EventInline, ClickInline]
    fieldsets = [
        ('', {'fields': ['uid', 'is_valid']}),
        ('Experiment', {'fields': ['location', 'device', 'polarization', 'attempt', 'timeout', 'regularity', 'colors', 'time_regularity_series']}),
        ('Dates', {'fields': ['start_datetime', 'end_datetime']}),
        ('Count', {'fields': ['count_all', 'count_blue', 'count_red', 'count_white']}),
        ('Tempo', {'fields': ['percentage_all', 'percentage_blue', 'percentage_red', 'percentage_white']}),
        ('Regularity', {'fields': ['time_stdev_all', 'time_stdev_blue', 'time_stdev_red', 'time_stdev_white']}),
        ('Interval', {'fields': ['time_mean_all', 'time_mean_blue', 'time_mean_red', 'time_mean_white']}),
    ]


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
class ClickAdmin(ImportExportModelAdmin, ValidateAction):
    list_display = ['datetime', 'is_valid', 'color']
    list_display_links = ['datetime']
    list_filter = ['is_valid', 'color']
    search_fields = ['=trial__id']
    ordering = ['-datetime']
    actions = ['make_invalid', 'make_valid']
