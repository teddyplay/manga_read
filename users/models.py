from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from users.managers import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=50,verbose_name="Иия фамилия",unique=True,)
    nickname = models.CharField(max_length=60,verbose_name="Ник",)
    image = models.ImageField(default="users_avatar")
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = [
        "nickname",
        "password",
    ]

    def __str__(self):
        return self.nickname
