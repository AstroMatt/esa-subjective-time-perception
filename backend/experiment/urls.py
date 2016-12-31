from django.conf.urls import url
from backend.api_v1.views import ExperimentResultCsvView
from backend.api_v1.views import ExperimentResultHtmlView


urlpatterns = [
    url(r'experiment/result.csv$', ExperimentResultCsvView.as_view()),
    url(r'experiment/result.html$', ExperimentResultHtmlView.as_view()),
]
