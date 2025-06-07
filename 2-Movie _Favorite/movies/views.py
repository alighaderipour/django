from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context = {
        'movies':['gladiator', 'up!', 'the hateful eight']
    }
    return render(request, 'movies/index.html', context)

def about(request):
    return render(request , 'movies/about.html', {})

# app/templates/app/index.html
# movies/templates/movies/index.html

