from django.db import models
from django.conf import settings

class Todo(models.Model):
    title = models.CharField(max_length=30)
    due_date = models.DateField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)