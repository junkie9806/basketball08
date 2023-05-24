from django.urls import path, include
from . import views

app_name='main'

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', include('search.urls', namespace='search')),
    path('login/',include('login.urls',namespace='login')),
]