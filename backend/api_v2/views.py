import datetime
from django.views.generic import TemplateView
from api_v2.models import Trial


class ReportRangeView(TemplateView):
    template_name = 'api_v2/report.html'

    def get_context_data(self, uid, start, end, **kwargs):
        current = datetime.datetime.strptime(start, '%Y-%m-%d')
        end_date = datetime.datetime.strptime(end, '%Y-%m-%d')
        delta = datetime.timedelta(days=1)

        results = []
        while current <= end_date:
            results.append({current: Trial.objects.filter(uid=uid, end_datetime__date=current)})
            current += delta

        return {'trials': results}


class ReportView(TemplateView):
    template_name = 'api_v2/report.html'

    def get_context_data(self, uid, **kwargs):
        return {'trials': Trial.objects.filter(uid=uid).order_by('-end_datetime')}
