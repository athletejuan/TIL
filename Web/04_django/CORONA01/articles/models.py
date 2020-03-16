from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.conf import settings

def article_image_path(instance, filename):
    return f'articles/{instance.id}번글/images/{filename}'

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    # image = models.ImageField(blank=True)
    image = ProcessedImageField(
        # upload_to = 'articles/images',              # 저장 위치
        upload_to = article_image_path,
        processors = [ResizeToFill(300, 200)],      # 처리할 작업 목록
        format = 'JPEG',                            # 저장 포맷
        options = {'quality': 90},                  # 옵션(이미지 품질 수치) -> 원본의 90% 정도의 품질
        blank = True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id}번 글: {self.title}'

class Comment(models.Model):
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    def __str__(self):
        return f'<article(self.articld_id) : Comment({self.id})> - {self.content}'