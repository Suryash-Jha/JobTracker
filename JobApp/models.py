from django.db import models

# Create your models here.

class JobModel(models.Model):
    StatusOptions=[
        ("AP", "Applied"),
        ("RJ", "Rejected"),
        ("NR", "No Response"),
        ("IV", "Interview"),
        ("OA", "Online Assessment"),
        ("AC", "Accepted"),
        ("AC", "Accepted"),
        ("RR", "Response Recieved")

    ]

    id = models.BigAutoField(primary_key=True)
    companyName= models.CharField(max_length=100)
    role= models.CharField(max_length=10)
    status= models.CharField(max_length=15, choices=StatusOptions)
    location= models.CharField(max_length=20)
    onsite= models.BooleanField(default=True)
    referralRecieved= models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.companyName+ str(self.id)
    



 

