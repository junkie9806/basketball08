from django import forms
from .models import TeamRegistration,Team

class TeamRegistrationForm(forms.ModelForm):
    class Meta:
        model = TeamRegistration
        fields = ['team']

class TeamForm(forms.ModelForm):    
    class Meta:
        model = Team
        fields = ['name', 'location','team_leader' ,'leader_permission']
