from django.db import models

class User(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    password = models.CharField(max_length=128)
    email = models.EmailField()
    phonenumber = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
