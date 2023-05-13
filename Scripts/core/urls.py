from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('competition/', views.competition_list, name='competition_list'),
    path('search/', views.search, name='search'),
    path('search/', views.search_view, name='search'),
]