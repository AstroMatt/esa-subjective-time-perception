from django.contrib import admin
from backend.logger.models import RequestLogger


@admin.register(RequestLogger)
class RequestLoggerAdmin(admin.ModelAdmin):
    list_display = ['datetime', 'ip', 'method', 'api_version']
    list_display_links = ['datetime']
    list_filter = ['method', 'api_version']
    ordering = ['-datetime']
