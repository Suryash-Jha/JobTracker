from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('hello/', views.hello),
    path('', views.home),
    path('list/', views.listJobs),
    path('add/', views.addJob),
    path('update/<str:id>', views.updateJob),
    path('delete/<str:id>', views.deleteJob),

    
]