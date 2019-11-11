from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

class Article(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    image = ProcessedImageField(
        upload_to = 'articles/images',
        processors = [ResizeToFill(200,300)],
        format = 'jpeg',
        options = {'quality': 90}
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-pk']

    def __str__(self):
        return f'No.{self.id} - {self.title}'

class Comment(models.Model):
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-pk']

    def __str__(self):
        return f'<Article({self.article_id}) : Comment({self.id})> - {self.content}'