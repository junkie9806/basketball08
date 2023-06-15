from django.shortcuts import render,redirect
from team.models import Team, TeamMember
from players.models import Player
from django.core.exceptions import ObjectDoesNotExist
from accounts_main.models import CustomUser

def team_main(request):
    team = Team.objects.all()
    return render(request, 'team/team_main.html', {'team' : team})

def create_team(request):
    if request.method == 'POST':
        teamname = request.POST.get('team_name')
        leader = request.user
        address = request.POST.get('address')
        
        team = Team.objects.create(teamname=teamname, leader=leader, address=address)
        
        leader.has_team = True
        leader.save()
        
        return redirect('main:team:manage_team_members')
    
    return render(request, 'team/create_team.html')

def manage_team_members(request):
    if request.method == 'POST':
        teamname = request.POST.get('teamname')
        leader = request.user
        playername = request.POST.get('playername')
        player = Player.objects.get(playername=playername)
        try:
            team = Team.objects.get(teamname=teamname)
        except ObjectDoesNotExist:
            # 팀이 존재하지 않는 경우 처리
            return redirect('main:team:team_main') 


        TeamMember.objects.create(team=team, leader=leader, player=player)
        return redirect('main:team:team_main')

    players = Player.objects.all()
    team = None
    return render(request, 'team/manage_team_members.html', {'players': players, 'team': team})
