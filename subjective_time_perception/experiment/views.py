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
        return {'experiments': Experiment.objects.filter(is_valid=True)}


class ExperimentResultCsvView(ExperimentResultMixin, TemplateView):
    template_name = 'experiment/results.csv'

    def get_output_data(self, experiment):
        """
        ID, WP1, WP2, WPW1, WPW2, WPR1, WPR2, WPB1, WPB2, WC1, WC2, WCW1, WCW2, WCR1, WCR2, WCB1, WCB2

        - ID użytkownika
        - WP1 - Współczynnik procentowy wszystkich - podejście 1
        - WP2 - Współczynnik procentowy wszystkich - podejście 2
        - WPW1 - Współczynnik procentowy białego - podejście 1
        - WPW2 - Współczynnik procentowy białego - podejście 2
        - WPR1 - Współczynnik procentowy czerwonego - podejście 1
        - WPR2 - Współczynnik procentowy czerwonego - podejście 2
        - WPB1 - Współczynnik procentowy niebieskiego - podejście 1
        - WPB2 - Współczynnik procentowy niebieskiego - podejście 2
        - WC1 - Współczynnik czasowy wszystkich - podejście 1 (odchylenie standardowe 60 środkowych interwałów czasowych wszystkich)
        - WC2 - Współczynnik czasowy wszystkich - podejście 2 (odchylenie standardowe 60 środkowych interwałów czasowych wszystkich)
        - WCW1 - Współczynnik czasowy białego - podejście 1 (odchylenie standardowe 20 środkowych interwałów czasowych białego)
        - WCW2 - Współczynnik czasowy białego - podejście 2 (odchylenie standardowe 20 środkowych interwałów czasowych białego)
        - WCR1 - Współczynnik czasowy czerwonego - podejście 1 (odchylenie standardowe 20 środkowych interwałów czasowych czerwonego)
        - WCR2 - Współczynnik czasowy czerwonego- podejście 2 (odchylenie standardowe 20 środkowych interwałów czasowych czerwonego)
        - WCB1 - Współczynnik czasowy niebieskiego - podejście 1 (odchylenie standardowe 20 środkowych interwałów czasowych niebieskiego)
        - WCB2 - Współczynnik czasowy niebieskiego - podejście 2 (odchylenie standardowe 20 środkowych interwałów czasowych niebieskiego)


        'experiment': e,
        'count': e.count_clicks(),
        'regularity_coefficient_percent': e.regularity_coefficient_percent(),
        'get_clicks_valid_for_experiment': e.get_clicks_valid_for_experiment(),
        #'regularity_coefficient_time': e.regularity_coefficient_time(),
        #'stdev': e.stdev(),
        #'mean': e.mean(),

        """

        return {
            'ID': experiment.id,
            'WP1': experiment.regularity_coefficient_percent()['all'],
            'WP2': None,
            'WPW1': experiment.regularity_coefficient_percent()['white'],
            'WPW2': None,
            'WPR1': experiment.regularity_coefficient_percent()['red'],
            'WPR2': None,
            'WPB1': experiment.regularity_coefficient_percent()['blue'],
            'WPB2': None,
            'WC1': experiment.stdev()['all'],
            'WC2': None,
            'WCW1': experiment.stdev()['white'],
            'WCW2': None,
            'WCR1': experiment.stdev()['red'],
            'WCR2': None,
            'WCB1': experiment.stdev()['blue'],
            'WCB2': None,
        }

    def get_context_data(self, *args, **kwargs):
        headers = ['ID', 'WP1', 'WP2', 'WPW1', 'WPW2', 'WPR1', 'WPR2', 'WPB1', 'WPB2', 'WC1', 'WC2', 'WCW1', 'WCW2', 'WCR1', 'WCR2', 'WCB1', 'WCB2']

        data = []

        return {'data': [self.get_output_data(e) for e in Experiment.objects.filter(is_valid=True)]}


class ExperimentResultHtmlView(ExperimentResultMixin, TemplateView):
    template_name = 'experiment/results.html'
