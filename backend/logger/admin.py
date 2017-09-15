from django.contrib import admin
from backend.logger.models import HTTPRequest


@admin.register(HTTPRequest)
class HTTPRequestAdmin(admin.ModelAdmin):
    change_list_template = 'admin/change_list_filter_sidebar.html'
    list_display = ['modified', 'ip', 'method', 'api_version', 'sha1']
    list_display_links = ['modified']
    list_filter = ['method', 'api_version', 'modified']
    search_fields = ['ip', 'sha1']
    ordering = ['-modified']
