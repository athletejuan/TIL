from django.db import models
from django.conf import settings
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

def articles_image_path(instance, filename):
    return f'articles/user_{instance.user.id}/images/{filename}'

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    # image = models.ImageField(blank=True)
    image = ProcessedImageField(
        upload_to = articles_image_path,
        processors = [ResizeToFill(300, 200)],
        format = 'png',
        options = {'quality':90},
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # AUTH_USER_MODEL : 장고가 기본적으로 갖고있는 유저 모델

    # blank 옵션은 좋아요를 누르지 않은 경우를 생각해서 True로 설정.
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles', blank=True)

    def __str__(self):
        return f'{self.id}: {self.title}'

class Comment(models.Model):
    content = models.CharField(max_length=100)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)    # 1 대 N 의 관계
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    # class Meta:
    #   ordering = ('-id',)