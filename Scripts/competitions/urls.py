
from django.urls import path
from . import views

urlpatterns = [
    path('', views.CompetitionListView.as_view(), name='competition_list'),
    path('<int:pk>/', views.CompetitionDetailView.as_view(), name='competition_detail'),
    # 추가 URL 정의
]
