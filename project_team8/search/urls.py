from django.urls import path
from search import views

app_name = 'search'

urlpatterns = [
    path('main/', views.player_search, name='player_search'),
    
]


