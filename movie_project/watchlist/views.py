from django.shortcuts import render
from .models import Movie
from django.http import JsonResponse

# Create your views here.

def movie(request):
    movies = Movie.objects.all()
    data = {
        'movies': list(movies.values())
        }   
    return  JsonResponse(data=data)

def movie_detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    data = {
        'movie': movie.title,
        'description': movie.description,
        'release_date': movie.release_date,
        'director': movie.director,
        'actors': movie.actors        
        }   
    return  JsonResponse(data)