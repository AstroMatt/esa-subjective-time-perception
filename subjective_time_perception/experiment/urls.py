from django.conf.urls import url
from django.views.generic import TemplateView
from subjective_time_perception.experiment.views import ExperimentCreateView


urlpatterns = [
    url(r'api/experiment/$', ExperimentCreateView.as_view()),
]
