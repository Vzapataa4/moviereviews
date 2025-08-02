from django.shortcuts import render
from .models import Movie

def home(request):
    search_query = request.GET.get('searchMovie')
    if search_query:
        movies = Movie.objects.filter(title__icontains=search_query)
    else:
        movies = Movie.objects.all()

    return render(request, 'home.html', {'movies': movies})

def about(request):
    return render(request, 'about.html')
