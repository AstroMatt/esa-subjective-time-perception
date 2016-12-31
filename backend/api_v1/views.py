import json
from django.http import JsonResponse
from django.views.generic import View
from backend.api_v1.models import Trial
from backend.logger.models import RequestLogger


class APIv1View(View):
    http_method_names = ['post']

    def post(self, request, *args, **kwargs):
        RequestLogger.add(request, api_version=1)
        try:
            trial = json.loads(request.body)
            Trial.add(**trial)
            response = JsonResponse({'message': 'Trial added to the database.'}, status=201)
        except json.decoder.JSONDecodeError:
            response = JsonResponse({'message': 'Cannot create trial'}, status=400)

        response['Access-Control-Allow-Origin'] = '*'
        return response
