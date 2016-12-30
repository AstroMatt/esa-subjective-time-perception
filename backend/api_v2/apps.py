from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class APIv2Config(AppConfig):
    name = 'backend.api_v2'
    label = 'api_v2'
    verbose_name = _('Experiment API v2')
