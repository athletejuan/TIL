from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

# def articles_image_path(instance, filename):
#     return f'articles/user_{instance.user.id}/images/{filename}'

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    # image = models.ImageField(blank=True)
    image = ProcessedImageField(
        upload_to='',
        processors=[ResizeToFill(300,200)],
        format='png',
        options={'quality':90},
        blank = True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.id}: {self.title}'
