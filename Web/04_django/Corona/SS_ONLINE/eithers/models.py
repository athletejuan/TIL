from django.db import models

class Question(models.Model):
    title = models.CharField(max_length=50)
    issue_a = models.CharField(max_length=50)
    issue_b = models.CharField(max_length=50)

class Comment(models.Model):
    pick = models.BooleanField()
    SELECT = [
        ['A', False],
        ['B', True],
    ]
    content = models.CharField(max_length=100)
    selecting = models.CharField(max_length=50, choices=SELECT)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)