from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    full_name = models.CharField(max_length=100, blank=True)
    contact_number = models.CharField(max_length=15, blank=True)
    bio = models.TextField(max_length=500, blank=True)
