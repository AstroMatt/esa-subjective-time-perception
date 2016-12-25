from django.conf.urls import url
from django.views.generic import TemplateView
from backend.experiment.api_v1 import TrialView
from backend.experiment.api_v1 import ExperimentResultCsvView
from backend.experiment.api_v1 import ExperimentResultHtmlView


urlpatterns = [
    url(r'trial/$', TrialView.as_view()),

    url(r'experiment/result.csv$', ExperimentResultCsvView.as_view()),
    url(r'experiment/result.html$', ExperimentResultHtmlView.as_view()),
]
