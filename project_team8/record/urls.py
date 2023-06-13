from django.urls import path
from record import views

app_name = 'record'

urlpatterns = [
    path('', views.record_main, name='record_main'),
    path('record_write/', views.record_write, name='record_write'),
]
