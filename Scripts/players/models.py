
from django.db import models

class Competition(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    # 추가 필드 정의

class Match(models.Model):
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE)
    team1 = models.CharField(max_length=100)
    team2 = models.CharField(max_length=100)
    # 추가 필드 정의
