from django.urls import path
from search import views

app_name = 'search'

urlpatterns = [
    path('main/', views.search_main, name='search_main'),
    
]


