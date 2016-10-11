import csv
import json
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.generic import View
from django.views.generic import TemplateView
from subjective_time_perception.experiment.models import Experiment


class ExperimentCreateView(View):
    http_method_names = ['post']

    def clean_data(self, data):
        return json.loads(data.replace('\n', ''))

    def post(self, request, *args, **kwargs):
        for record in self.clean_data(request.body.decode('utf-8')):
            Experiment.add(**record)
        response = JsonResponse({'status': 'ok', 'code': 200})
        response['Access-Control-Allow-Origin'] = '*'
        return response


class ExperimentResultMixin:
    def get_context_data(self, *args, **kwargs):
        experiments = Experiment.objects.all()
        return {'experiments': experiments}


class ExperimentResultCsvView(ExperimentResultMixin, TemplateView):
    template_name = 'experiment/results.csv'


class ExperimentResultHtmlView(ExperimentResultMixin, TemplateView):
    template_name = 'experiment/results.html'
