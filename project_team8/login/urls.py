
from django.urls import path
from login import views

app_name = 'login'

urlpatterns = [
    path('', views.login_main, name='login_main'),
    path('register/', views.login_register, name='login_register'),
    path('kakaoLoginLogic/', views.kakaoLoginLogic, name="kakoLoginLogic"),
    path('kakaoLoginLogicRedirect/', views.kakaoLoginLogicRedirect, name="kakaoLoginLogicRedirect"),
    path('kakaoLogout/', views.kakaoLogout, name="kakaoLogout"),
]
