from django.conf.urls import url
from django.views.generic import TemplateView
from backend.experiment.views import ExperimentCreateView
from backend.experiment.views import ExperimentResultCsvView
from backend.experiment.views import ExperimentResultHtmlView


urlpatterns = [
    url(r'experiment/$', ExperimentCreateView.as_view()),

    url(r'experiment/result.csv$', ExperimentResultCsvView.as_view()),
    url(r'experiment/result.html$', ExperimentResultHtmlView.as_view()),
]
