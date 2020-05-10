from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=20)

class Music(models.Model):
    title = models.CharField(max_length=100)
    artist = models.ForeignKey(Artist, related_name='musics', on_delete=models.CASCADE)

class Comment(models.Model):
    content = models.CharField(max_length=200)
    music = models.ForeignKey(Music, related_name='comments', on_delete=models.CASCADE)
