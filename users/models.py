from django.db import models
from django.contrib.auth.models import AbstractUser
from config.models_utils.models import TimeStampModel


class User(AbstractUser):
    email = models.EmailField(unique=True)
    phone_numer = models.CharField(unique=True, max_length=32)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return f"{self.email} ({self.phone_numer})"



    

