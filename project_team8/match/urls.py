from django.urls import path
from .views import match_list, create_match, join_match, match_main

app_name ='match'

urlpatterns = [
    path('match-list/', match_list, name='match_list'),
    path('match-main/', match_main, name='match_main' ),
    path('create-match/', create_match, name='create_match'),
    path('join-match/<int:match_id>/', join_match, name='join_match'),
]
