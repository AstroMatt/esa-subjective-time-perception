from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class APIv1Config(AppConfig):
    name = 'backend.api_v1'
    label = 'api_v1'
    verbose_name = _('Experiment API v1')
