from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

def hello(req):
    data= {"status": "hello"}
    return JsonResponse(data)
# Create your views here.


