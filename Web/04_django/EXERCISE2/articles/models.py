from django.db import models
from django.conf import settings
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = ProcessedImageField(
        upload_to = '',                             # 저장 위치
        processors = [ResizeToFill(200, 300)],      # 처리할 작업 목록
        format = 'JPEG',                            # 저장 포멧
        options = {'quality':90},                   # 옵션(이미지 품질 수치)
    )
    # image = models.ImageField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles', blank=True)

    class Meta:
        ordering = ['-pk']

    def __str__(self):
        return f'{self.id}: {self.title}'

class Comment(models.Model):
    content = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    # models.OneToOne()
    # models.ManyToMany()

    class Meta:
        ordering = ['-pk']
