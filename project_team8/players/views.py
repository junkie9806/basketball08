from django.shortcuts import render, redirect
from .models import Player

def player_main(request):
    players = Player.objects.all()
    return render(request, 'players/player_main.html', {'players' : players})

def add_player(request):
    if request.method == 'POST':
        name = request.POST['name']
        height = request.POST['height']
        weight = request.POST['weight']
        position = request.POST['position']
        player = Player(name=name, height=height, weight=weight, position=position)
        player.save()
        return redirect('main:players:add_player')
    return render(request, 'players/add_player.html')

def player_form(request):
    # 선수 정보 수정 기능 구현
    return render(request, 'players/player_form.html')

def player_list(request):
    # 선수 목록 조회 기능 구현 
    players = Player.objects.all()
    return render(request, 'players/player_list.html', {'players' : players})

# Create your views here.
