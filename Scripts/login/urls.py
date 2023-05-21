
from django.urls import path
from . import views

app_name = 'login'

urlpatterns = [
    path('', views.login_main, name='login_main'),
    path('', views.login_view, name='login'),
    path('register/', views.login_register, name='login_register'),
]
