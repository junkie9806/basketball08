from django.db import models
from accounts_main.models import CustomUser

class Player(models.Model):
    #name = models.CharField(max_length=100)
    playername = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='players', default=None)
    height = models.FloatField()
    weight = models.FloatField()
    position = models.CharField(max_length=100)

    def __str__(self):
        return self.playername
        