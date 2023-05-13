from django.views.generic import ListView, DetailView
from .models import Competition

class CompetitionListView(ListView):
    model = Competition
    template_name = 'competitions/competition_list.html'
    # 추가 필요한 로직 구현

class CompetitionDetailView(DetailView):
    model = Competition
    template_name = 'competitions/competition_detail.html'
    # 추가 필요한 로직 구현
