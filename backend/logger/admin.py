from django.contrib import admin
from backend.logger.models import HTTPRequest
from backend.logger.models import ErrorLogger
from import_export.admin import ImportExportModelAdmin


@admin.register(HTTPRequest)
class HTTPRequestAdmin(ImportExportModelAdmin):
    change_list_template = 'admin/change_list_import_export.html'
    change_list_filter_template = 'admin/filter_listing.html'
    list_display = ['modified', 'ip', 'method', 'api_version', 'sha1']
    list_display_links = ['modified']
    list_filter = ['method', 'api_version', 'modified']
    search_fields = ['ip', 'sha1']
    ordering = ['-modified']
    list_per_page = 10


@admin.register(ErrorLogger)
class ErrorLoggerAdmin(ImportExportModelAdmin):
    change_list_template = 'admin/change_list_import_export.html'
    change_list_filter_template = 'admin/filter_listing.html'
    list_display = ['added', 'http_request_sha1']
    list_display_links = ['http_request_sha1']
    list_filter = ['added']
    search_fields = ['^http_request_sha1', '^added']
    ordering = ['-modified']
    list_per_page = 10
