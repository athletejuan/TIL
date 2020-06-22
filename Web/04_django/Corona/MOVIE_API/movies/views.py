from django.shortcuts import render
from .models import Movie
from rest_framework.decorators import api_view

@api_view(['GET'])
def movies_list(request):
    movies = Movie.objects.all()