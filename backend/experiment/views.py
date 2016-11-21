import csv
import json
import logging
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.generic import View
from django.views.generic import TemplateView
from backend.experiment.models import Experiment
from backend.experiment.models import Trial

log = logging.getLogger('backend')



class ExperimentView(View):
    http_method_names = ['post']

    def post(self, request, *args, **kwargs):
        """
        [
            {
                "start": "2016-11-21T14:35:39.938Z",
                "end": "2016-11-21T14:35:59.998Z",
                "trial": {
                    "number": 1,
                    "location": "Experiment over the internet",
                    "device": "computer 1",
                    "polarization": "horizontal",
                    "colors": [
                        "blue",
                        "red",
                        "white"
                    ]
                },
                "data": [
                    {
                        "datetime": "2016-11-21T14:35:39.939Z",
                        "target": "trial",
                        "action": "start"
                    },
                    {
                        "datetime": "2016-11-21T14:35:42.830Z",
                        "target": "survey",
                        "action": "start"
                    },
                    {
                        "datetime": "2016-11-21T14:35:51.959Z",
                        "target": "survey",
                        "action": "end"
                    },
                    {
                        "datetime": "2016-11-21T14:35:53.048Z",
                        "target": "black",
                        "action": "start"
                    },
                    {
                        "datetime": "2016-11-21T14:35:53.050Z",
                        "target": "black",
                        "action": "click"
                    },
                    {
                        "datetime": "2016-11-21T14:35:53.735Z",
                        "target": "black",
                        "action": "click"
                    },
                    {
                        "datetime": "2016-11-21T14:35:53.896Z",
                        "target": "black",
                        "action": "click"
                    },
                    {
                        "datetime": "2016-11-21T14:35:54.031Z",
                        "target": "black",
                        "action": "click"
                    },
                    {
                        "datetime": "2016-11-21T14:35:54.051Z",
                        "target": "black",
                        "action": "end"
                    },
                    {
                        "datetime": "2016-11-21T14:35:55.072Z",
                        "target": "blue",
                        "action": "start"
                    },
                    {
                        "datetime": "2016-11-21T14:35:55.072Z",
                        "target": "blue",
                        "action": "click"
                    },
                    {
                        "datetime": "2016-11-21T14:35:55.383Z",
                        "target": "blue",
                        "action": "click"
                    },
                    {
                        "datetime": "2016-11-21T14:35:55.551Z",
                        "target": "blue",
                        "action": "click"
                    },
                    {
                        "datetime": "2016-11-21T14:35:55.688Z",
                        "target": "blue",
                        "action": "click"
                    },
                    {
                        "datetime": "2016-11-21T14:35:55.831Z",
                        "target": "blue",
                        "action": "click"
                    },
                    {
                        "datetime": "2016-11-21T14:35:55.975Z",
                        "target": "blue",
                        "action": "click"
                    },
                    {
                        "datetime": "2016-11-21T14:35:56.074Z",
                        "target": "blue",
                        "action": "end"
                    },
                    {
                        "datetime": "2016-11-21T14:35:56.929Z",
                        "target": "red",
                        "action": "start"
                    },
                    {
                        "datetime": "2016-11-21T14:35:56.930Z",
                        "target": "red",
                        "action": "click"
                    },
                    {
                        "datetime": "2016-11-21T14:35:57.207Z",
                        "target": "red",
                        "action": "click"
                    },
                    {
                        "datetime": "2016-11-21T14:35:57.367Z",
                        "target": "red",
                        "action": "click"
                    },
                    {
                        "datetime": "2016-11-21T14:35:57.519Z",
                        "target": "red",
                        "action": "click"
                    },
                    {
                        "datetime": "2016-11-21T14:35:57.647Z",
                        "target": "red",
                        "action": "click"
                    },
                    {
                        "datetime": "2016-11-21T14:35:57.814Z",
                        "target": "red",
                        "action": "click"
                    },
                    {
                        "datetime": "2016-11-21T14:35:57.932Z",
                        "target": "red",
                        "action": "end"
                    },
                    {
                        "datetime": "2016-11-21T14:35:58.801Z",
                        "target": "white",
                        "action": "start"
                    },
                    {
                        "datetime": "2016-11-21T14:35:58.802Z",
                        "target": "white",
                        "action": "click"
                    },
                    {
                        "datetime": "2016-11-21T14:35:59.103Z",
                        "target": "white",
                        "action": "click"
                    },
                    {
                        "datetime": "2016-11-21T14:35:59.271Z",
                        "target": "white",
                        "action": "click"
                    },
                    {
                        "datetime": "2016-11-21T14:35:59.423Z",
                        "target": "white",
                        "action": "click"
                    },
                    {
                        "datetime": "2016-11-21T14:35:59.575Z",
                        "target": "white",
                        "action": "click"
                    },
                    {
                        "datetime": "2016-11-21T14:35:59.743Z",
                        "target": "white",
                        "action": "click"
                    },
                    {
                        "datetime": "2016-11-21T14:35:59.803Z",
                        "target": "white",
                        "action": "end"
                    },
                    {
                        "datetime": "2016-11-21T14:35:59.999Z",
                        "target": "trial",
                        "action": "end"
                    }
                ],
                "survey": {
                    "email": "a@a.pl",
                    "age": "23",
                    "gender": "male",
                    "condition": "normal",
                    "rhythm": "average"
                }
            },
            {
                "start": "2016-11-21T14:36:05.390Z",
                "end": "2016-11-21T14:36:27.324Z",
                "trial": {
                    "number": 2,
                    "location": "Experiment over the internet",
                    "device": "computer 1",
                    "polarization": "horizontal",
                    "colors": [
                        "white",
                        "blue",
                        "red"
                    ]
                },
                "data": [
                    {
                        "datetime": "2016-11-21T14:36:05.391Z",
                        "target": "trial",
                        "action": "start"
                    },
                    {
                        "datetime": "2016-11-21T14:36:06.454Z",
                        "target": "survey",
                        "action": "start"
                    },
                    {
                        "datetime": "2016-11-21T14:36:18.709Z",
                        "target": "survey",
                        "action": "end"
                    },
                    {
                        "datetime": "2016-11-21T14:36:20.431Z",
                        "target": "black",
                        "action": "start"
                    },
                    {
                        "datetime": "2016-11-21T14:36:20.432Z",
                        "target": "black",
                        "action": "click"
                    },
                    {
                        "datetime": "2016-11-21T14:36:21.268Z",
                        "target": "black",
                        "action": "click"
                    },
                    {
                        "datetime": "2016-11-21T14:36:21.405Z",
                        "target": "black",
                        "action": "click"
                    },
                    {
                        "datetime": "2016-11-21T14:36:21.432Z",
                        "target": "black",
                        "action": "end"
                    },
                    {
                        "datetime": "2016-11-21T14:36:22.375Z",
                        "target": "white",
                        "action": "start"
                    },
                    {
                        "datetime": "2016-11-21T14:36:22.375Z",
                        "target": "white",
                        "action": "click"
                    },
                    {
                        "datetime": "2016-11-21T14:36:22.684Z",
                        "target": "white",
                        "action": "click"
                    },
                    {
                        "datetime": "2016-11-21T14:36:22.836Z",
                        "target": "white",
                        "action": "click"
                    },
                    {
                        "datetime": "2016-11-21T14:36:22.988Z",
                        "target": "white",
                        "action": "click"
                    },
                    {
                        "datetime": "2016-11-21T14:36:23.116Z",
                        "target": "white",
                        "action": "click"
                    },
                    {
                        "datetime": "2016-11-21T14:36:23.261Z",
                        "target": "white",
                        "action": "click"
                    },
                    {
                        "datetime": "2016-11-21T14:36:23.377Z",
                        "target": "white",
                        "action": "end"
                    },
                    {
                        "datetime": "2016-11-21T14:36:24.287Z",
                        "target": "blue",
                        "action": "start"
                    },
                    {
                        "datetime": "2016-11-21T14:36:24.288Z",
                        "target": "blue",
                        "action": "click"
                    },
                    {
                        "datetime": "2016-11-21T14:36:24.580Z",
                        "target": "blue",
                        "action": "click"
                    },
                    {
                        "datetime": "2016-11-21T14:36:24.740Z",
                        "target": "blue",
                        "action": "click"
                    },
                    {
                        "datetime": "2016-11-21T14:36:24.892Z",
                        "target": "blue",
                        "action": "click"
                    },
                    {
                        "datetime": "2016-11-21T14:36:25.039Z",
                        "target": "blue",
                        "action": "click"
                    },
                    {
                        "datetime": "2016-11-21T14:36:25.180Z",
                        "target": "blue",
                        "action": "click"
                    },
                    {
                        "datetime": "2016-11-21T14:36:25.289Z",
                        "target": "blue",
                        "action": "end"
                    },
                    {
                        "datetime": "2016-11-21T14:36:26.142Z",
                        "target": "red",
                        "action": "start"
                    },
                    {
                        "datetime": "2016-11-21T14:36:26.142Z",
                        "target": "red",
                        "action": "click"
                    },
                    {
                        "datetime": "2016-11-21T14:36:26.484Z",
                        "target": "red",
                        "action": "click"
                    },
                    {
                        "datetime": "2016-11-21T14:36:26.644Z",
                        "target": "red",
                        "action": "click"
                    },
                    {
                        "datetime": "2016-11-21T14:36:26.788Z",
                        "target": "red",
                        "action": "click"
                    },
                    {
                        "datetime": "2016-11-21T14:36:26.948Z",
                        "target": "red",
                        "action": "click"
                    },
                    {
                        "datetime": "2016-11-21T14:36:27.108Z",
                        "target": "red",
                        "action": "click"
                    },
                    {
                        "datetime": "2016-11-21T14:36:27.144Z",
                        "target": "red",
                        "action": "end"
                    },
                    {
                        "datetime": "2016-11-21T14:36:27.326Z",
                        "target": "trial",
                        "action": "end"
                    }
                ],
                "survey": {
                    "email": "a@a.pl",
                    "age": "23",
                    "gender": "male",
                    "condition": "normal",
                    "rhythm": "average"
                }
            }
        ]
        """
    
    
        data = request.body.decode('utf-8').replace('\n', '')
        experiment = json.loads(data)
        
        try:
            Experiment.add(**experiment)
            response = JsonResponse({'message': 'Experiment added to the database.'}, status=201)
        except Exception:
            response = JsonResponse({'message': 'Cannot create experiment'}, status=400)
            
        response['Access-Control-Allow-Origin'] = '*'
        return response
        





class ExperimentResultCsvView(TemplateView):
    template_name = 'experiment/results.csv'

    def get_output_data(self, experiment):
        log.warning('Calculating results for: {}'.format(experiment))
        """
        - ID użytkownika
        - name
        - start_date
        - polarization

        - C1 - Ilość kliknięć wszystkich - podejście 1
        - CW1 - Ilość kliknięć białych - podejście 1
        - CR1 - Ilość kliknięć czerwonych - podejście 1
        - CB1 - Ilość kliknięć niebieskich - podejście 1

        - PC1 - Współczynnik procentowy wszystkich - podejście 1
        - PC2 - Współczynnik procentowy wszystkich - podejście 2
        - PCW1 - Współczynnik procentowy białego - podejście 1
        - PCW2 - Współczynnik procentowy białego - podejście 2
        - PCR1 - Współczynnik procentowy czerwonego - podejście 1
        - PCR2 - Współczynnik procentowy czerwonego - podejście 2
        - PCB1 - Współczynnik procentowy niebieskiego - podejście 1
        - PCB2 - Współczynnik procentowy niebieskiego - podejście 2

        - TCSD1 - Współczynnik czasowy wszystkich - podejście 1 (odchylenie standardowe 60 środkowych interwałów czasowych wszystkich)
        - TCSD2 - Współczynnik czasowy wszystkich - podejście 2 (odchylenie standardowe 60 środkowych interwałów czasowych wszystkich)
        - TCSDW1 - Współczynnik czasowy białego - podejście 1 (odchylenie standardowe 20 środkowych interwałów czasowych białego)
        - TCSDW2 - Współczynnik czasowy białego - podejście 2 (odchylenie standardowe 20 środkowych interwałów czasowych białego)
        - TCSDR1 - Współczynnik czasowy czerwonego - podejście 1 (odchylenie standardowe 20 środkowych interwałów czasowych czerwonego)
        - TCSDR2 - Współczynnik czasowy czerwonego- podejście 2 (odchylenie standardowe 20 środkowych interwałów czasowych czerwonego)
        - TCSDB1 - Współczynnik czasowy niebieskiego - podejście 1 (odchylenie standardowe 20 środkowych interwałów czasowych niebieskiego)
        - TCSDB2 - Współczynnik czasowy niebieskiego - podejście 2 (odchylenie standardowe 20 środkowych interwałów czasowych niebieskiego)

        - TCM1 - Średnia 60 środkowych interwałów czasowych wszystkich - podejście 1
        - TCMW1 - Średnia 60 środkowych interwałów czasowych białych - podejście 1
        - TCMR1 - Średnia 60 środkowych interwałów czasowych czerwonych - podejście 1
        - TCMB1 - Średnia 60 środkowych interwałów czasowych niebieskich - podejście 1
        """

        return {
            'ID': experiment.id,
            'name': '{last_name} {first_name}'.format(**experiment.__dict__),
            'polarization': experiment.polarization,
            'start_date': experiment.experiment_start,

            'C1': experiment.count_clicks()['all'],
            'CW1': experiment.count_clicks()['white'],
            'CR1': experiment.count_clicks()['red'],
            'CB1': experiment.count_clicks()['blue'],

            'PC1': experiment.regularity_coefficient_percent()['all'],
            'PCW1': experiment.regularity_coefficient_percent()['white'],
            'PCR1': experiment.regularity_coefficient_percent()['red'],
            'PCB1': experiment.regularity_coefficient_percent()['blue'],

            'TCSD1': experiment.stdev()['all'],
            'TCSDW1': experiment.stdev()['white'],
            'TCSDR1': experiment.stdev()['red'],
            'TCSDB1': experiment.stdev()['blue'],

            'TCM1': experiment.mean()['all'],
            'TCMW1': experiment.mean()['white'],
            'TCMR1': experiment.mean()['red'],
            'TCMB1': experiment.mean()['blue'],
        }

    def get_context_data(self, *args, **kwargs):
        return {'results': [self.get_output_data(e) for e in Experiment.get()]}


class ExperimentResultHtmlView(TemplateView):
    template_name = 'experiment/results.html'
