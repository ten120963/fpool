from django import forms
from .models import picks, teams, games

class picksForm(forms.ModelForm):
	class Meta:
		model = picks
		fields = ["name", "email", "afce", "afcn", "afcs", "afcw", "nfce", "nfcn", "nfcs", "nfcw"]

class CalculateForm(forms.Form):
    btn = forms.CharField()	

class CalculateTeamForm(forms.Form):
    btn = forms.CharField()	    
    fields = ["week"]

class teamsForm(forms.ModelForm):
	class Meta:
		model = teams
		fields = ["team", "division", "status"]    

class gamesForm(forms.ModelForm):

	class Meta:
		model = games
		fields = ["week", "away", "awayscore", "home", "homescore"]  			