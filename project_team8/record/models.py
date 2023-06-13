from django.db import models

# Create your models here.
class Record(models.Model):
    record_name = models.CharField(max_length=20)
    score = models.IntegerField(default=0)
    assist = models.IntegerField(default=0)
    rebound = models.IntegerField(default=0)
    steal = models.IntegerField(default=0)
    block = models.IntegerField(default=0)
    
    
    
    def __str__(self):
        return self.player_name

