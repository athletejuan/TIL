from django.db import models

class Question(models.Model):
    title = models.CharField(max_length=50)
    issue_a = models.CharField(max_length=50)
    issue_b = models.CharField(max_length=50)

class Comment(models.Model):
    pick = models.BooleanField()
    content = models.CharField(max_length=100)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)