from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager


class CustomUser(AbstractUser):
    username = None
    phone_number = models.CharField(max_length=10, unique=True)
    email = models.EmailField(unique=True, null=True)
    user_bio = models.CharField(max_length=100)
    user_image = models.ImageField(upload_to="profile")
    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = []
    objects = UserManager()

    def __str__(self):
        return self.phone_number
