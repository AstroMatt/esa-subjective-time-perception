import json
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.generic import View
from subjective_time_perception.experiment.models import Experiment



class ExperimentCreateView(View):
    http_method_names = ['post', 'put', 'update']

    def clean_data(self, data):
        return json.loads(data.replace('\n', ''))

    def update(self, *args, **kwargs):
        for experiment in Experiment.objects.all():
            experiment.date = Event.objects.filter(experiment=experiment, action='start', message='experiment')[0].datetime
            experiment.save()
        return JsonResponse({})

    def put(self, *args, **kwargs):
        filename = '/developer/esa-act-subjective-time-perception/data/2016-10-02-esa.int-subjective-time-perception-data2.json'
        experiments = []
        with open(filename) as file:
            for record in self.clean_data(file.read()):
                e = Experiment.add(**record)
                experiments.append(e)
        return JsonResponse(experiments, safe=False)

    def post(self, request, *args, **kwargs):
        for record in self.clean_data(request.body.decode('utf-8')):
            Experiment.add(**record)
        response = JsonResponse({'status': 'ok', 'code': 200})
        response['Access-Control-Allow-Origin'] = '*'
        return response

        #response = HttpResponse(my_data, content_type='application/vnd.ms-excel')
        #response['Content-Disposition'] = 'attachment; filename="foo.xls"'
