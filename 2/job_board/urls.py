from django.contrib import admin
from django.urls import path
from .views import index, job_details

urlpatterns = [
    path('', index, name='home'),
    path('job/', index, name='home'),
]
