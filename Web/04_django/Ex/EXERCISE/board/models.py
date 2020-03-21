from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:   # views에 걸리는 부하를 저감,
        ordering = ['-pk']

    def __str__(self):
        return f'{self.id}. {self.title}'

class Comment(models.Model):
    content = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE) # 반(1)을 삭제시 해당 반 소속학생(N) 같이 연동삭제(CASCADE)
    # models.OneToOne()
    # models.ManyToMany()

    class Meta:   # views에 걸리는 부하를 저감,
        ordering = ['-pk']