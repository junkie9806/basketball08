from django.urls import path
from . import views

app_name='board'

urlpatterns = [
    path('', views.board_main, name='board_main'),
    path('write/', views.write, name='write'),
    
]
