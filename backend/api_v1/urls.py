from django.conf.urls import url
from backend.api_v1.views import APIv1View


urlpatterns = [
    url(r'$', APIv1View.as_view()),
]
