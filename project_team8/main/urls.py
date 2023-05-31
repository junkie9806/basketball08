from django.urls import path, include
from . import views

app_name='main'

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', include('search.urls', namespace='search')),
    path('accounts1/',include('accounts1.urls', namespace='accounts1')),
    path('players/',include('players.urls',namespace='players')),
    path('board/',include('board.urls',namespace='board')),
]