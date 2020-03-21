from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill, Thumbnail
from django.conf import settings

def articles_image_path(instance, filename):
    return f'articles/{instance.pk}번 글/images/{filename}'
    # 경로: MEDIA_ROOT/articles/{instance.pk}번 글/images/{filename}
    # instance --> 파라미터 instance는 Article 모델의 객체를 의미한다.
    # filename --> 업로드한 이미지 파일의 이름 

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = ProcessedImageField(
        # upload_to='articles/images',        # 저장위치(MEDIA_ROOT/articles/images)
        upload_to=articles_image_path,
        processors=[ResizeToFill(300,200)], # 처리할 작업 목록
        format='png',                       # 저장 포맷
        options={'quality': 90},            # 추가 옵션들
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles', blank=True)
    
    class Meta:
        ordering = ['-pk']

    def __str__(self):
        return f'{self.id}. {self.title}'

class Comment(models.Model):
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-pk']

    def __str__(self):
        return f'<Article({self.article_id} : Comment({self.id})> - {self.content}'
    