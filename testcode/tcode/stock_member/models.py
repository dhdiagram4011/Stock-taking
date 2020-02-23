from django.db import models

from django.contrib.auth.models import AbstractUser
#from django.contrib.auth import get_user_model


class User(AbstractUser):
    depart = models.CharField(max_length=500)
    position = models.CharField(max_length=500)
    phone = models.CharField(max_length=500)
    floor = models.IntegerField(max_length=500)
    email = models.EmailField(max_length=1000)