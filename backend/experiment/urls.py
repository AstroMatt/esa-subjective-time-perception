from django.conf.urls import url
from django.views.generic import TemplateView
from backend.experiment.views import ExperimentView
from backend.experiment.views import ExperimentResultCsvView
from backend.experiment.views import ExperimentResultHtmlView


urlpatterns = [
    url(r'experiment/$', ExperimentView.as_view()),

    url(r'experiment/result.csv$', ExperimentResultCsvView.as_view()),
    url(r'experiment/result.html$', ExperimentResultHtmlView.as_view()),
]
