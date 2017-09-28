from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class APIv3Config(AppConfig):
    name = 'backend.api_v3'
    label = 'api_v3'
    verbose_name = _('API v3')
