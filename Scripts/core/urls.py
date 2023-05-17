from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('competition/', views.competition_list, name='competition_list'),
    path('search/', views.search, name='search'),
    path('search/', views.search_view, name='search'),
    path('players/', include('players.urls', namespace='players')),
    path('login/', include('login.urls', namespace='login')),
]