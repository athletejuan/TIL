from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()    
    created_at = models.DateTimeField(auto_now_add=True)
    image_url = models.TextField()

    def __str__(self):
        return f'{self.id}: {self.title}'