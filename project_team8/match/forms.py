from django import forms
from .models import Match

class CreateMatchForm(forms.ModelForm):
    class Meta:
        model = Match
        fields = ['team_name_1', 'match_date', 'location']
