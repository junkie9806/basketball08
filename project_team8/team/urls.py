from django.urls import path
from team import views

app_name = 'team'

urlpatterns = [
    path('', views.team_main, name='team_main'),
    path('register/', views.team_register, name='team_register'),
    path('accept/<int:registration_id>/', views.team_accept_registration, name='team_accept_registration'),
    path('create/', views.create_team, name='team_create'),
]
