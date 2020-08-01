from django.conf.urls import url
from backend.api_v1.views import APIv1View

app_name = 'api_v1'

urlpatterns = [
    url(r'$', APIv1View.as_view()),
]
