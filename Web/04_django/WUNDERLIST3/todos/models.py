from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=30)
    due_date = models.DateField()
