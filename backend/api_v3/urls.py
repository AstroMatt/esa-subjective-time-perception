from django.conf.urls import url
from backend.api_v3.views import APIv3View


urlpatterns = [
    url(r'$', APIv3View.as_view()),
]
