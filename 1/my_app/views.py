from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("hello world")

def about(request):
    return HttpResponse("I am Ali Ghaderi Pour and I am going to be a great programmer")


def hello(request, first_name):
    return HttpResponse(f"Hello {first_name}, YOU ARE THE BEST")


def sumTwoNumber(request,num1, num2):
    sumz = num1 + num2
    return HttpResponse(f"{sumz}")