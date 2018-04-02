from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    # nickname을 추가 (blank=True)
    img_profile = models.ImageField(upload_to='user', blank=True)
    nickname = models.CharField(max_length=30, blank=True)

