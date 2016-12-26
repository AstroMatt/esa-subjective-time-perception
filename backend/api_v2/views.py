import json
import logging
from django.http import JsonResponse
from django.views.generic import View
from backend.api_v2.models import Trial

log = logging.getLogger('backend')



class TrialView(View):
    http_method_names = ['post', 'get']

    def get(self, *args, **kwargs):
        with open('/developer/esa-act-subjective-time-perception/temp/api_v2-trial2.json') as file:
            import json
            content = json.loads(file.read())
        trial = Trial.add(**content)
        return JsonResponse(trial, status=201, safe=False)

    def post(self, request, *args, **kwargs):
        data = request.body.decode('utf-8').replace('\n', '')
        trial = json.loads(data)

        try:
            Trial.add(**trial)
            response = JsonResponse({'message': 'Trial added to the database.'}, status=201)
        except Exception:
            response = JsonResponse({'message': 'Cannot create trial'}, status=400)

        response['Access-Control-Allow-Origin'] = '*'
        return response
