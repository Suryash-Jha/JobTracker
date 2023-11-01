from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from django import forms
from .models import JobModel


class JobData(forms.ModelForm):
    class Meta:
        model= JobModel
        fields=(
            "companyName",
            "role",
            "status",
            "location",
            "onsite",
            "referralRecieved"
        )

def hello(req):
    data= {"status": "hello"}
    return JsonResponse(data)

def home(req):
    data={"status": "home"}
    return render(req, "JobApp\index.html")

@csrf_exempt
def addJob(request):
    statusCode = 200
    status = ""

    if request.method == "POST":
        try:
            form = JobData(request.POST)
            if form.is_valid():
                form.save()

        except Exception as e:
            statusCode = 404
            status = "Failed to save data" + str(e)
    else:
        form = JobData()
    return render(
        request,
        "JobApp\\addJob.html",
        {"form": form, "status": status, "statusCode": statusCode},
    )
# @csrf_exempt
# def addJob(req):
#     statusCode = 200

#     if req.method == "POST":
#         form = JobData(req.POST)
#         if form.is_valid():
#             form.save()
#         else:
#             print("saved")
#         return JsonResponse({"statusCode": statusCode, "FORM": str(form), "post": str(req.POST)})

#     else:
#         data = JobModel.objects.all()
#         for i in data:
#             print(i.companyName + " applied on " + str(i.updated_at))
#         form = JobData()
#     return render(req, "JobApp\\addJob.html", {"form": form, "statusCode": statusCode})

def updateJob(req, id):
    data= {"status": "hello", "id": id}
    return JsonResponse(data)

def deleteJob(req, id):
    data= {"status": "hello", "id": id}
    return JsonResponse(data)

def listJobs(req):
    data= JobModel.objects.all()
    finalDict=[]
    for i in data:

        x={}
        x['companyName']= i.companyName
        x['role']= i.role
        x['status']= i.get_status_display()
        x['statusKey']= i.status
        x['location']= i.location
        x['onsite']= i.onsite
        x['referralRecieved']= i.referralRecieved
        x['created_at']= int(i.created_at.timestamp())
        x['updated_at']= int(i.updated_at.timestamp())

        finalDict.append(x)
    return render(req, "JobApp\listJob.html", context={"data" : finalDict})



# Create your views here.


