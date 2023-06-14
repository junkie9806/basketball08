from django.urls import path
from team.views import create_team, manage_team_members, team_main

app_name = 'team'
urlpatterns = [
    path('create/', create_team, name='create_team'),
    path('team/manage/', manage_team_members, name='manage_team_members'),  # 새로운 URL 패턴 추가
    path('team/manage/<int:team_id>/', manage_team_members, name='manage_team_members'),  # 기존 URL 패턴 유지
    path('team_main/', team_main, name='team_main'),
]
