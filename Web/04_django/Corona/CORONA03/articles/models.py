from django.db import models
from django.urls import reverse
from django.conf import settings
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail

# def articles_image_path(instance, filename):
#     return f'user_{instance.user.pk}/{filename}'

class Article(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    # image = models.ImageField(blank=True, upload_to='%Y/%m/%d/')
    # image = models.ImageField(blank=True, upload_to=articles_image_path)
    image = ProcessedImageField(
        blank=True,
        processors=[Thumbnail(200,300)],
        format='JPEG',
        options={'quality': 90},
        upload_to='%Y/%m/%d',
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    # def get_absolute_url(self):
    #     return reverse('articles:detail', args=[self.pk])
        
    def get_absolute_url(self):
        return reverse("articles:detail", kwargs={"pk": self.pk})

    def __str__(self):
        return f'{self.pk}번 글 - {self.title}'


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content