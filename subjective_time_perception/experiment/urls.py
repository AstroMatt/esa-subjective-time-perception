from django.conf.urls import url
from django.views.generic import TemplateView
from subjective_time_perception.experiment.views import ExperimentCreateView
from subjective_time_perception.experiment.views import CSVExportView


urlpatterns = [
    url(r'experiment/api/$', ExperimentCreateView.as_view()),
    url(r'experiment/export/csv/$', CSVExportView.as_view()),
]
