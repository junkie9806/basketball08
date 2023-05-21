from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=11)
    address = models.CharField(max_length=100)
