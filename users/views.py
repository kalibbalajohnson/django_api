from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt 
def create(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        return JsonResponse({"message": "App is running", "received": data})
    return JsonResponse({"error": "Invalid request method."}, status=400)


def get(request):
    return HttpResponse("app is running")
