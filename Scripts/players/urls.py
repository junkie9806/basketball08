from django.urls import path
from players import views

app_name = 'players'

urlpatterns = [
    path('main/', views.player_main, name='player_main'),
    path('add/', views.add_player, name='add_player'),
    path('form/', views.player_form, name='player_form'),
    path('list/', views.player_list, name='player_list'),
]
