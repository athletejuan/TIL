from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=20)
    title_en = models.CharField(max_length=50)
    audience = models.IntegerField()
    open_date = models.DateField()
    genre = models.CharField(max_length=20)
    watch_grade = models.CharField(max_length=10)
    score = models.FloatField()
    poster_url = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return f'{self.title}: {self.score}'