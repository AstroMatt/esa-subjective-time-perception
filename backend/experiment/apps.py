from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class ExperimentConfig(AppConfig):
    name = 'backend.experiment'
    label = 'experiment'
    verbose_name = _('Experiment')
