from django.db import models
from django.urls import reverse

class Article(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # def get_absolute_url(self):
    #     return reverse('articles:detail', args=[self.pk])
        
    def get_absolute_url(self):
        return reverse("articles:detail", kwargs={"pk": self.pk})

    def __str__(self):
        return f'{self.pk}번 글 - {self.title}'