# from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    avatar = models.URLField(default=None, blank=True, max_length=200)

    class Meta:
        ordering = ["date_joined"]

    def __str__(self):
        return {
            self.username,
            self.first_name,
            self.last_name,
            self.date_joined,
            self.avatar,
        }
