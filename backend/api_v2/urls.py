from django.conf.urls import url
from django.views.generic import TemplateView
from backend.api_v2.views import TrialView


urlpatterns = [
    url(r'trial/$', TrialView.as_view()),
]
