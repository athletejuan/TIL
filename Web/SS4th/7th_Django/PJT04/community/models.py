from django.db import models

class Review(models.Model):
    title = models.CharField(max_length=100)
    movie_title = models.CharField(max_length=50)
    content = models.TextField()
    rank = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'No.{self.pk} - {self.title}'