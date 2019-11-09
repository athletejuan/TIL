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