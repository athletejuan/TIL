from django.shortcuts import render

def movies_list(request):
    movies = Movie.objects.all()