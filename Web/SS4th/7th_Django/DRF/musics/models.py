from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=20)


class Music(models.Model):
    title = models.CharField(max_length=100)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)