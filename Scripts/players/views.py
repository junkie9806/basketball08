from django.shortcuts import render, redirect
from .forms import PlayerForm
from .models import Player

def player_main(request):
    return render(request, 'players/player_main.html')

def add_player(request):
    added_player=None
    if request.method == 'POST':
        form = PlayerForm(request.POST)
        if form.is_valid():
            added_player = form.save()
            return redirect('players:add_player') # 선수 추가 후 리디렉션
    else:
        form = PlayerForm()
        added_player = None
        

    context = {
        'form': form,
        'added_player': added_player
    }

    return render(request, 'players/add_player.html', context)

def player_form(request):
    # 선수 정보 수정 기능 구현
    return render(request, 'players/player_form.html')

def player_list(request):
    # 선수 목록 조회 기능 구현
    return render(request, 'players/player_list.html')
