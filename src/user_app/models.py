from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    email=models.EmailField(unique=True,blank=True)
    phone=models.CharField(max_length=15)
    nationalite=models.CharField(max_length=125)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['phone','username']

