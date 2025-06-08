from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'favorite_movies':['up!', 'the gadfather', 'seven']
    }
    return render(request, 'movies/index.html', context)

def about(request):
    return render(request, 'movies/about.html', {})