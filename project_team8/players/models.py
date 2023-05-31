from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=100)
    height = models.FloatField()
    weight = models.FloatField()
    position = models.CharField(max_length=100)

    def __str__(self):
        return self.name
