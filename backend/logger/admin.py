from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from backend.logger.models import HTTPRequest
from import_export.admin import ImportExportModelAdmin


class RequestsWithoutResultsFilter(admin.SimpleListFilter):
    title = _('Requests without Results')
    parameter_name = 'need_recalculate'

    def lookups(self, request, model_admin):
        return [
            ('yes', _('Need recalculate')),
        ]

    def queryset(self, request, queryset):
        from backend.api_v3.models import Result

        all_results = Result.objects.all().values_list('request_sha1', flat=True)

        if self.value() == 'yes':
            return queryset.exclude(sha1__in=list(all_results))


@admin.register(HTTPRequest)
class HTTPRequestAdmin(ImportExportModelAdmin):
    change_list_template = 'admin/change_list_import_export.html'
    change_list_filter_template = 'admin/filter_listing.html'
    actions = ['recalculate', 'mark_as_problematic']
    list_display = ['integrity', 'field_datetime', 'ip', 'method', 'api_version', 'sha1', 'error_log']
    list_display_links = ['field_datetime']
    list_filter = ['integrity', RequestsWithoutResultsFilter, 'method', 'api_version', 'modified']
    search_fields = ['ip', 'sha1']
    ordering = ['-modified']
    list_per_page = 100
    readonly_fields = ['sha1', 'ip', 'method', 'api_version']

    def field_datetime(self, obj):
        return f'{obj.added:%Y-%m-%d %H:%M}'

    field_datetime.admin_order_field = 'datetime'
    field_datetime.short_description = _('Datetime [UTC]')

    def mark_as_problematic(modeladmin, request, queryset):
        queryset.update(integrity=HTTPRequest.INTEGRITY_ERROR)

    def recalculate(modeladmin, request, queryset):
        import json
        from backend.api_v3.models import Result
        from backend._common.utils import json_datetime_decoder

        for request in queryset:
            data = json.loads(request.data, object_hook=json_datetime_decoder)
            Result.add(
                request_sha1=request.sha1,
                clicks=data.pop('clicks'),
                result=data,
            )

    recalculate.short_description = _('Recalculate Results from HTTP Request')

    class Media:
        css = {'all': [
            'logger/css/httprequest-resize-body.css',
        ]}
