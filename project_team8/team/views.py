from django.shortcuts import render,redirect
from team.models import Team, TeamMember
from players.models import Player

def team_main(request):
    team = Team.objects.all()
    return render(request, 'team/team_main.html', {'team' : team})

def create_team(request):
    if request.method == 'POST':
        team_name = request.POST.get('team_name')
        leader = request.user
        address = request.POST.get('address')
        
        team = Team.objects.create(name=team_name, leader=leader, address=address)
        
        # 팀 ID를 세션에 저장
        request.session['team_id'] = team.id
        
        return render(request, 'team/create_team.html', {'team': team})
    
    return render(request, 'team/create_team.html')

def manage_team_members(request):
    if request.method == 'POST':
        leader = request.user
        player_id = request.POST.get('player_id')
        player = Player.objects.get(id=player_id)
        TeamMember.objects.create(leader=leader, player=player)
        return redirect('main:team:team_main')

    players = Player.objects.all()
    return render(request, 'team/manage_team_members.html', {'players': players})
