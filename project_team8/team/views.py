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
        playername = request.POST.get('player')

        try:
            player = Player.objects.get(playername=playername)
            TeamMember.objects.create(leader=leader, player=player)
            return redirect('main:team:team_main')  # Redirect to the appropriate URL
        except Player.DoesNotExist:
            error_message = f"Player '{playername}' does not exist."
            return render(request, 'team/manage_team_members.html', {'error_message': error_message})
