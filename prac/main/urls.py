from django.urls import path, include
from . import views

app_name='main'

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', include('search.urls', namespace='search')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    #path('login/',include('login.urls',namespace='login')),
    path('players/',include('players.urls',namespace='players')),
    path('board/',include('board.urls',namespace='board')),
]