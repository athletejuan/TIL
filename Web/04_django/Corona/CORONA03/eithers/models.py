from django.db import models
from django.conf import settings

class Question(models.Model):
    title = models.CharField(max_length=20)
    select_A = models.CharField(max_length=20)
    select_B = models.CharField(max_length=20)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Comment(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    CHOICES = [
        ['Blue', False],
        ['Red', True],
    ]
    pick = models.BooleanField()
    select = models.CharField(max_length=20, choices=CHOICES)
    content = models.CharField(max_length=200)