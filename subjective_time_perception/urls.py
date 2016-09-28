from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin


urlpatterns = [
    url(r'^', admin.site.urls),
    url(r'^', include('subjective_time_perception.experiment.urls')),
]
