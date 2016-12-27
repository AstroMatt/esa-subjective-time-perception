import json
import logging
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.generic import View
from backend.api_v2.models import Trial

log = logging.getLogger('backend')


class TrialView(View):
    http_method_names = ['post', 'head']

    def head(*args, **kwargs):
        response = HttpResponse(status=200)
        response['Access-Control-Allow-Origin'] = '*'
        return response

    def post(self, request, *args, **kwargs):
        try:
            data = request.body.decode('utf-8').replace('\n', '')
            trial = json.loads(data)
            Trial.add(**trial)
            response = JsonResponse({'message': 'Trial added to the database.'}, status=201)
        except Exception:
            response = JsonResponse({'message': 'Cannot create trial'}, status=400)

        response['Access-Control-Allow-Origin'] = '*'
        return response
