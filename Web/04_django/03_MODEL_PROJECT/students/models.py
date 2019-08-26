from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=10)
    email = models.CharField(max_length=50)
    github_id = models.CharField(max_length=50)
    age = models.IntegerField()

class Menu(models.Model):
    name = models.CharField(max_length=20)
    price = models.FloatField()
    category = models.CharField(max_length=10)