from django.db import models

class Question(models.Model):
    title = models.CharField(max_length=20)
    select_A = models.CharField(max_length=20)
    select_B = models.CharField(max_length=20)


class Comment(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    select = models.BooleanField()
    content = models.CharField(max_length=200)