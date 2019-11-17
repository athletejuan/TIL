from django.db import models
from django.conf import settings
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill, Thumbnail

def articles_image_path(instance, filename):
    return f'articles/user.{instance.user.pk}/images/{filename}'

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    # image = models.ImageField(blank=True)         # 기본 이미지 업로드
    image = ProcessedImageField(
        upload_to = articles_image_path,            # 저장 위치
        # upload_to = '',                           # 저장 위치(/media/)
        processors = [ResizeToFill(300, 200)],      # 처리할 작업 목록[이미지 사이즈 조정(가로300px, 세로200px)]
        # processors = [Thumbnail(100, 100)],       # 처리할 작업 목록[Thumbnail 사이즈(가로100px, 세로100px)]
        format = 'png',                             # 저장 포멧
        options = {'quality':90},                   # 옵션(이미지 품질 수치)
        blank = True,                               # 빈 값 허용
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles', blank=True)

    # article = Article.objects.get(id=1)
    # user -> admin

    #1. 1:N
    # article.user # 게시글을 쓴 유저(admin)
    # user.article_set.all() # 유저(admin)가 쓴 게시글 전체 (겹침)

    #2. M:N
    # article.like_users # 1번 게시글을 좋아요 한 유저
    # user.article_set.all() # 유저가 좋아요 한 게시글 전체 (겹침)
    # --> user.like_articles.all() # 유저(admin)이 좋아요를 누른 모든 게시글들

    def __str__(self):
        return f'{self.id}: {self.title}'

class Comment(models.Model):
    content = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)    # 1 대 N 의 관계
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
