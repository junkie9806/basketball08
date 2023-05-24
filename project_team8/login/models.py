from django.db import models

# Create your models here.
class User(models.Model):
    user_id=models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=11)
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=100)
