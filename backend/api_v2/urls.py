from django.conf.urls import url
from backend.api_v2.views import APIv2View


urlpatterns = [
    url(r'$', APIv2View.as_view()),
]
