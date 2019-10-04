from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    followers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='followings')

# 팔로우: 특정 대상을 팔로우하는 경우 그 대상의 소식을 받아볼 수 있다.
# 팔로잉: 나 또는 특정 대상이 팔로우하는 사람
# 팔로워: 나 또는 특정 대상을 팔로우하는 사람