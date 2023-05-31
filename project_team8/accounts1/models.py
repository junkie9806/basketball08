from django.db import models

class User(models.Model):  # 1
    username = models.CharField(max_length=255)
    useremail = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self): # 2
        return self.username