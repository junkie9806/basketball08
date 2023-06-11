from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # 추가 필드 정의
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    leader = models.BooleanField(False)

    class Meta:
        db_table = 'login_user'