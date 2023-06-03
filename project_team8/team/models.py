from django.db import models
from django.contrib.auth.models import User

class Team(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    team_leader = models.ForeignKey(User, on_delete=models.CASCADE)    
    leader_permission = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class TeamMember(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team_members')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='team_memberships')
    is_accepted = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username} - {self.team.name}'

class TeamRegistration(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='registrations')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='team_registrations')

    def __str__(self):
        return f'{self.user.username} - {self.team.name}'