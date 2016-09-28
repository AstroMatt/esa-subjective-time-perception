from datetime import datetime
import json
from django.http import JsonResponse
from django.http import HttpResponse
from django.views.generic import View
from subjective_time_perception.experiment.models import Experiment
from subjective_time_perception.experiment.models import Click


class ExperimentCreateView(View):
    http_method_names = ['post']

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body.decode('utf-8'))

        experiment, status = Experiment.objects.get_or_create(
            first_name=data.get('first_name'),
            last_name=data.get('last_name'),
            age=data.get('age'),
            gender=data.get('gender'),
            rhythm=data.get('rhythm'),
            condition=data.get('condition'),
            start_date=datetime.strptime(data.get('start_date'), '%Y-%m-%dT%H:%M:%S.%fZ'),
            end_date=datetime.strptime(data.get('end_date'), '%Y-%m-%dT%H:%M:%S.%fZ'),
        )

        for click in data.get('click'):
            Click.objects.get_or_create(
                experiment=experiment,
                datetime=datetime.strptime(click.get('datetime'), '%Y-%m-%dT%H:%M:%S.%fZ'),
                background=click.get('background'),
            )

        response = HttpResponse(data, content_type='application/json')
        response['Access-Control-Allow-Origin'] = '*'
        return response




        #return JsonResponse(request.POST)
        #return JsonResponse({'status':200, 'message': 'OK'})

        #response = HttpResponse(my_data, content_type='application/vnd.ms-excel')
        #response['Content-Disposition'] = 'attachment; filename="foo.xls"'
