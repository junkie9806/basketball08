from django.db import models
from players.models import Player
from accounts_main.models import CustomUser

class Team(models.Model):
    name = models.CharField(max_length=200)
    leader = models.ForeignKey(CustomUser, on_delete=models.CASCADE,default=None)
    address = models.CharField(max_length=200)
    # 다른 필요한 필드들을 추가하세요

    def __str__(self):
        return self.name
    class Meta:
        db_table = 'team_team'

class TeamMember(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='members')
    leader = models.ForeignKey(CustomUser, on_delete=models.CASCADE,default=None)
    playername = models.ForeignKey(Player, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.team.name} - {self.player.playername}"
    class Meta:
        db_table = 'team_member'
