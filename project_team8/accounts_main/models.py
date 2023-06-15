from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # 추가 필드 정의
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    leader = models.BooleanField(default=None)
    has_team = models.BooleanField(default=False)

    def __str__(self):
        return self.first_name

    class Meta:
        db_table = 'login_user'