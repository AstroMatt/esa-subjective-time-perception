from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from backend.logger.models import HTTPRequest
from backend.logger.models import ErrorLogger
from import_export.admin import ImportExportModelAdmin


@admin.register(HTTPRequest)
class HTTPRequestAdmin(ImportExportModelAdmin):
    change_list_template = 'admin/change_list_import_export.html'
    change_list_filter_template = 'admin/filter_listing.html'
    actions = ['recalculate']
    list_display = ['modified', 'ip', 'method', 'api_version', 'sha1']
    list_display_links = ['modified']
    list_filter = ['method', 'api_version', 'modified']
    search_fields = ['ip', 'sha1']
    ordering = ['-modified']
    list_per_page = 10
    readonly_fields = ['sha1', 'ip', 'method', 'api_version']

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


@admin.register(ErrorLogger)
class ErrorLoggerAdmin(ImportExportModelAdmin):
    change_list_template = 'admin/change_list_import_export.html'
    change_list_filter_template = 'admin/filter_listing.html'
    list_display = ['added', 'request_sha1']
    list_display_links = ['request_sha1']
    list_filter = ['added']
    search_fields = ['^request_sha1', '^added']
    ordering = ['-modified']
    list_per_page = 10
