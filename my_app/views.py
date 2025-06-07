from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    print("request is ", request)
    return HttpResponse("hello world")

def about(request):
    return HttpResponse("I am Ali Ghaderi Pour and I am going to be a great programmer")