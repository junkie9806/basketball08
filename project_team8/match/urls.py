from django.urls import path
from .views import match_list, create_match, join_match

app_name ='match'

urlpatterns = [
    path('matches/', match_list, name='match_list'),
    path('create-match/', create_match, name='create_match'),
    path('join-match/<int:match_id>/', join_match, name='join_match'),
]
