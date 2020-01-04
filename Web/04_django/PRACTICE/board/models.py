from django.db import models
from django.conf import settings
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

def board_image_path(instance, filename):
    return f'board/{instance.pk}번 글/images/{filename}'
    # return f'board/{instance.user.pk}번 글/images/{filename}'

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = ProcessedImageField(
        # upload_to = 'board/images',             # 저장위치
        upload_to = board_image_path,           # 저장위치
        processors = [ResizeToFill(300, 200)],  # 처리할 작업 목록[Resize Image(width 300px, height 200px)]
        format = 'png',                         # 저장 포멧
        options = {'quality':90},               # 옵션(이미지 품질 수치) -> 원본의 90% 품질
    )
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles', blank=True)

    def __str__(self):
        return f'{self.id}. {self.title}'

class Comment(models.Model):
    content = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.content}'

