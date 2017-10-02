from django.conf.urls import url
from backend.api_v3 import api
from backend.api_v3 import views


urlpatterns = [
    url(r'report/(?P<uid>.+)/$', views.ReportView.as_view(), name='report'),
    url(r'$', api.APIv3.as_view(), name='api'),
]
