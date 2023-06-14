from django.urls import path
from team.views import create_team, manage_team_members, team_main

app_name = 'team'
urlpatterns = [
    path('create/', create_team, name='create_team'),
    path('manage/', manage_team_members, name='manage_team_members'),
    path('team_main/', team_main, name='team_main'),
]
