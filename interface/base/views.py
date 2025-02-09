import json
from django.views.generic import TemplateView
from django.http import JsonResponse
from functions.util import predict  

class DrawView(TemplateView):
    template_name = 'draw.html'

    def post(self, request, *args, **kwargs):
        try:
            prediction = predict(request.body)
            return JsonResponse({"prediction": prediction})
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
