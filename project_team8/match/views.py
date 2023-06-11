from django.shortcuts import render, redirect
from .forms import CreateMatchForm
from accounts_main.forms import CustomUser
from .models import Match

def match_list(request):
    matches = Match.objects.all()
    context = {'matches': matches}
    if CustomUser.leader == True:
        return render(request, 'match/match_main.html', context)
    else:
        return render(request, 'match/match_list.html', context)

def create_match(request):
    if request.method == 'POST':
        form = CreateMatchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:match:match_list')
    else:
        form = CreateMatchForm()
    return render(request, 'match/create_match.html', {'form': form})

def join_match(request, match_id):
    match = Match.objects.get(id = match_id)
    if request.method == 'POST':
        team_name_2 = request.POST.get('team_name_2')
        match.team_name_2 = team_name_2
        match.is_joined = True  # 매치에 참가한 경우 is_joined를 True로 설정
        match.save()  # 변경된 정보를 저장
        return redirect('main:match:match_list')
    else:
        return render(request, 'match/join_match.html', {'match' : match})