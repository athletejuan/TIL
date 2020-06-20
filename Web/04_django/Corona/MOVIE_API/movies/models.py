from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=20)
        
class Movie(models.Model):
    title = models.CharField(max_length=30)
    audience = models.IntegerField()
    poster_url = models.TextField()
    description = models.TextField()
    genre = models.ForeignKey(Genre, related_name='movies', on_delete=models.CASCADE)
    
class Score(models.Model):
    content = models.CharField(max_length=140)
    score = models.IntegerField()
    movie = models.ForeignKey(Movie, related_name='scores', on_delete=models.CASCADE)