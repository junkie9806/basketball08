from django.db import models

class Match(models.Model):
    team_name_1 = models.CharField(max_length=100)
    team_name_2 = models.CharField(max_length=100)
    match_date = models.DateTimeField()
    location = models.CharField(max_length=100)
    is_joined = models.BooleanField(False)

    def __str__(self):
        return self.team_name
