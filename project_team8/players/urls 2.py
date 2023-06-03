from django.urls import path
from players import views

app_name = 'players'

urlpatterns = [
    path('player_main/', views.player_main, name='player_main'),
    path('add_player/', views.add_player, name='add_player'),
    path('player_form/', views.player_form, name='player_form'),
    path('player_list/', views.player_list, name='player_list'),
]
