from django.shortcuts import render, redirect, get_object_or_404
from .models import Team, TeamMember, TeamRegistration
from .forms import TeamRegistrationForm

def team_main(request):
    teams = Team.objects.all()
    return render(request, 'team/team_main.html', {'teams': teams})

def team_register(request):
    
    if request.method == 'POST':
        form = TeamRegistrationForm(request.POST)
        if form.is_valid():
            registration = form.save(commit=False)
            registration.user = request.user
            registration.save()
            return redirect('main:team:team_main')
    else:
        form = TeamRegistrationForm()
    return render(request, 'team/team_register.html', {'form': form})

def team_accept_registration(request, registration_id):
    teams = Team.objects.all()
    registration = get_object_or_404(TeamRegistration, id=registration_id)
    if registration.team.leader == request.user:
        team = registration.team
        user = registration.user

        # 등록 요청 수락 처리
        TeamMember.objects.create(team=team, user=user)
        registration.is_accepted = True
        registration.save()

    return redirect('main:team:team_main')

from django.shortcuts import render, redirect
from .forms import TeamForm
from .models import Team

def create_team(request):
    
    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            team = form.save(commit=False)
            team.leader = request.user
            team.save()
            return redirect('main:team:team_main')
    else:
        form = TeamForm()
    return render(request, 'team/team_register.html', {'form': form})

