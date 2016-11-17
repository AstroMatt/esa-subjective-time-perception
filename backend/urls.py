import os
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
from django.views.generic import RedirectView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/v1/', include('backend.experiment.urls')),

    url(r'^$', RedirectView.as_view(url='/index.html', permanent=False)),
] + static(r'/', document_root=os.path.join(settings.BASE_DIR, 'frontend'))
