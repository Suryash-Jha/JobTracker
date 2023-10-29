from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

def hello(req):
    data= {"status": "hello"}
    return JsonResponse(data)

def home(req):
    data={"status": "home"}
    return JsonResponse(data)

def addJob(req):
    data= {"status": "hello"}
    return JsonResponse(data)

def updateJob(req, id):
    data= {"status": "hello", "id": id}
    return JsonResponse(data)

def deleteJob(req, id):
    data= {"status": "hello", "id": id}
    return JsonResponse(data)

def listJobs(req):
    arr= [3, 3, 5]
    data= {"status": "hello", "arr": arr}


# Create your views here.


