from django.shortcuts import render
from django.views   import View
from django.http    import JsonResponse, HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def home(request):
    return render(request, "user/login.html")


