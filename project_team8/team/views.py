from django.shortcuts import render,redirect
from team.models import Team, TeamMember
from players.models import Player
from accounts_main.models import CustomUser

def team_main(request):
    team = Team.objects.all()
    return render(request, 'team/team_main.html', {'team' : team})

def create_team(request):
    if request.method == 'POST':
        team_name = request.POST.get('team_name')
        leader = request.user
        address = request.POST.get('address')
        
        team = Team.objects.create(name=team_name, leader=leader, address=address)
        
        leader.profile.has_team = True
        leader.profile.save()
        
        return redirect('main:team:manage_team_members', team_id=team.id)
    
    return render(request, 'team/create_team.html')

def manage_team_members(request, team_id):
    if request.method == 'POST':
        leader = request.user
        playername = request.POST.get('playername')
        player = Player.objects.get(playername=playername)
        team = Team.objects.get(id=team_id)


        TeamMember.objects.create(team=team, leader=leader, player=player)
        return redirect('main:team:team_main')

    players = Player.objects.all()
    team = Team.objects.get(id=team_id)
    return render(request, 'team/manage_team_members.html', {'players': players, 'team': team})
