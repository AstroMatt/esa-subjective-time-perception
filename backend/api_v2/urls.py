from django.conf.urls import url
from backend.api_v2 import api
from backend.api_v2 import views


urlpatterns = [
    url(r'report/(?P<uid>.+)/(?P<start>.+)/(?P<end>.+)/$', views.ReportRangeView.as_view(), name='report-range'),
    url(r'report/(?P<uid>.+)/$', views.ReportView.as_view(), name='report'),
    url(r'$', api.APIv2.as_view(), name='api'),
]
