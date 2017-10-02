from django.views.generic import TemplateView
from backend.api_v3.models import Result


class ReportView(TemplateView):
    template_name = 'api_v3/report.html'

    def get_context_data(self, uid, **kwargs):
        return {'trials': Result.objects.filter(uid=uid).order_by('-end_datetime')}
