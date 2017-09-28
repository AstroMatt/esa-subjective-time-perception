from django.contrib import admin
from backend.logger.models import HTTPRequest
from backend.logger.models import ErrorLogger


@admin.register(HTTPRequest)
class HTTPRequestAdmin(admin.ModelAdmin):
    change_list_template = 'admin/change_list_filter_sidebar.html'
    list_display = ['modified', 'ip', 'method', 'api_version', 'sha1']
    list_display_links = ['modified']
    list_filter = ['method', 'api_version', 'modified']
    search_fields = ['ip', 'sha1']
    ordering = ['-modified']
    list_per_page = 10


@admin.register(ErrorLogger)
class ErrorLoggerAdmin(admin.ModelAdmin):
    change_list_template = 'admin/change_list_filter_sidebar.html'
    list_display = ['modified', 'http_request_sha1']
    list_display_links = ['http_request_sha1']
    list_filter = ['modified']
    search_fields = ['^http_request_sha1']
    ordering = ['-modified']
    list_per_page = 10
