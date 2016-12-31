from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class LoggerConfig(AppConfig):
    name = 'backend.logger'
    label = 'logger'
    verbose_name = _('Logger')
