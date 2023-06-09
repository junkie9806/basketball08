from django.db import models

class Match(models.Model):
    team_name = models.CharField(max_length=100)
    match_date = models.DateTimeField()
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.team_name
