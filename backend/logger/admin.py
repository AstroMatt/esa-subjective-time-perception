from django.contrib import admin
from backend.logger.models import RequestLogger
from backend.logger.models import HTTPRequest

@admin.register(RequestLogger)
class RequestLoggerAdmin(admin.ModelAdmin):
    change_list_template = 'admin/change_list_filter_sidebar.html'
    list_display = ['datetime', 'ip', 'method', 'api_version', 'sha1']
    list_display_links = ['datetime']
    list_filter = ['method', 'api_version']
    search_fields = ['ip', 'sha1']
    ordering = ['-datetime']


@admin.register(HTTPRequest)
class HTTPRequestAdmin(admin.ModelAdmin):
    change_list_template = 'admin/change_list_filter_sidebar.html'
    list_display = ['datetime', 'ip', 'method', 'api_version', 'sha1']
    list_display_links = ['datetime']
    list_filter = ['method', 'api_version']
    search_fields = ['ip', 'sha1']
    ordering = ['-datetime']
