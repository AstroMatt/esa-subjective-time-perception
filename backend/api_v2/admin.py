from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from import_export.admin import ImportExportModelAdmin

from backend.api_v2.models import Event, Click
from backend.api_v2.models import Survey
from backend.api_v2.models import Trial


class TempoListFilter(admin.SimpleListFilter):
    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = _('Tempo all')

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'tempo_all'

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
            return queryset.filter(tempo_all__gt=200)

        if self.value() == 'fast':
            return queryset.filter(tempo_all__gt=125, tempo_all__lte=200)

        if self.value() == 'normal':
            return queryset.filter(tempo_all__gte=75, tempo_all__lte=125)

        if self.value() == 'slow':
            return queryset.filter(tempo_all__gte=25, tempo_all__lt=75)

        if self.value() == 'too-few':
            return queryset.filter(tempo_all__lt=25)


class ValidateAction:
    def make_invalid(modeladmin, request, queryset):
        queryset.update(is_valid=False)
    make_invalid.short_description = _('Mark as invalid')

    def make_valid(modeladmin, request, queryset):
        queryset.update(is_valid=True)
    make_valid.short_description = _('Mark as valid')


class SurveyInline(admin.StackedInline):
    model = Survey
    classes = ['collapse open']
    inline_classes = ['collapse open']
    extra = 0


@admin.register(Trial)
class TrialAdmin(ImportExportModelAdmin, ValidateAction):
    change_list_template = 'api_v2/admin-links.html'
    change_list_filter_template = 'admin/filter_listing.html'
    list_display = ['is_valid', 'field_date', 'time', 'uid', 'field_hash', 'timeout',  'regularity', 'count_all', 'tempo_all', 'regularity_all', 'interval_all']
    list_display_links = ['field_date']
    list_editable = ['uid', 'time']
    list_filter = [TempoListFilter, 'time', 'uid', 'end_datetime', 'is_valid', 'polarization', 'timeout', 'regularity', 'colors', 'device', 'location']
    search_fields = ['=id', '^uid', '^http_request_sha1', '^end_datetime']
    ordering = ['-end_datetime']
    actions = ['make_invalid', 'make_valid']
    inlines = [SurveyInline]
    list_per_page = 20
    fieldsets = [
        ('', {'fields': ['uid', 'is_valid', 'start_datetime', 'end_datetime', 'time']}),
        ('Summary', {'fields': ['count_all', 'tempo_all', 'regularity_all', 'interval_all']}),
        ('Count', {'fields': ['count_all', 'count_blue', 'count_red', 'count_white']}),
        ('Tempo', {'fields': ['tempo_all', 'tempo_blue', 'tempo_red', 'tempo_white']}),
        ('Regularity', {'fields': ['regularity_all', 'regularity_blue', 'regularity_red', 'regularity_white']}),
        ('Interval', {'fields': ['interval_all', 'interval_blue', 'interval_red', 'interval_white']}),
        ('Details', {'fields': ['device', 'location', 'timeout', 'regularity', 'colors', 'time_between_clicks']})
    ]

    def field_date(self, obj):
        return f'{obj.end_datetime:%Y-%m-%d %H:%M}'

    field_date.short_description = _('Datetime')
    field_date.admin_order_field = 'end_datetime'

    def field_hash(self, obj):
        if obj.http_request_sha1:
            return f'{obj.http_request_sha1:.7}'
        else:
            return f'n/a'

    field_hash.short_description = _('Hash')
    field_hash.admin_order_field = 'http_request_sha1'


@admin.register(Survey)
class SurveyAdmin(ImportExportModelAdmin):
    change_list_template = 'admin/change_list_import_export.html'
    change_list_filter_template = 'admin/filter_listing.html'
    list_display = ['datetime', 'email', 'age', 'condition', 'gender', 'rhythm', 'trial']
    list_display_links = ['datetime']
    list_filter = ['gender', 'condition', 'rhythm', 'age']
    search_fields = ['^email', '^datetime']
    ordering = ['-datetime']


# @admin.register(Event)
class EventAdmin(ImportExportModelAdmin):
    change_list_template = 'admin/change_list_import_export.html'
    change_list_filter_template = 'admin/filter_listing.html'
    list_display = ['datetime', 'target', 'action', 'trial']
    list_display_links = ['datetime']
    list_filter = ['target', 'action']
    search_fields = ['=trial__id']
    ordering = ['-datetime']


# @admin.register(Click)
class ClickAdmin(ImportExportModelAdmin, ValidateAction):
    change_list_template = 'admin/change_list_import_export.html'
    change_list_filter_template = 'admin/filter_listing.html'
    list_display = ['datetime', 'is_valid', 'color']
    list_display_links = ['datetime']
    list_filter = ['is_valid', 'color']
    search_fields = ['=trial__id']
    ordering = ['-datetime']
    actions = ['make_invalid', 'make_valid']
