from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=30)
    due_date = models.DateField()

    def __str__(self):
        return f'{ self.id }: { self.title }'
