import csv
import json
import logging
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.generic import View
from django.views.generic import TemplateView
from backend.api_v1.models import Experiment
from backend.api_v1.models import Trial

log = logging.getLogger('backend')



class APIv1View(View):
    http_method_names = ['post']

    def post(self, request, *args, **kwargs):
        try:
            trial = json.loads(request.body)
            Trial.add(**trial)
            response = JsonResponse({'message': 'Trial added to the database.'}, status=201)
        except json.decoder.JSONDecodeError:
            response = JsonResponse({'message': 'Cannot create trial'}, status=400)

        response['Access-Control-Allow-Origin'] = '*'
        return response
