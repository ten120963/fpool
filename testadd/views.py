from django.shortcuts import render, redirect
from .models import picks, teams, games
from .forms import picksForm, CalculateForm, teamsForm, gamesForm
from django.contrib import messages
from django.views.generic import TemplateView, ListView
from django.db.models import Q # new

class SearchResultsView(ListView):
    model = games
    template_name = 'search_results.html'

    def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list = games.objects.filter(
            Q(week=query)
        )
        return object_list


def picks_valid():
	all_teams = teams.objects.all()
	
	last_status = 0
	playoff_status = 0
	
	for cur_team in all_teams:
		current_team = cur_team.team
		current_status = cur_team.status
		if afce_team == current_team:
			if current_status == "P":
				playoff_status = playoff_status + 1
			if current_status == "L":
				last_status = last_status + 1	
		if afcn_team == current_team:
			if current_status == "P":
				playoff_status = playoff_status + 1
			if current_status == "L":
				last_status = last_status + 1	
		if afcs_team == current_team:
			if current_status == "P":
				playoff_status = playoff_status + 1
			if current_status == "L":
				last_status = last_status + 1	
		if afcw_team == current_team:
			if current_status == "P":
				playoff_status = playoff_status + 1
			if current_status == "L":
				last_status = last_status + 1	
		if nfce_team == current_team:
			if current_status == "P":
				playoff_status = playoff_status + 1
			if current_status == "L":
				last_status = last_status + 1	
		if nfcn_team == current_team:
			if current_status == "P":
				playoff_status = playoff_status + 1
			if current_status == "L":
				last_status = last_status + 1	
		if nfcs_team == current_team:
			if current_status == "P":
				playoff_status = playoff_status + 1
			if current_status == "L":
				last_status = last_status + 1	
		if nfcw_team == current_team:
			if current_status == "P":
				playoff_status = playoff_status + 1
			if current_status == "L":
				last_status = last_status + 1
	if playoff_status > 4 or last_status < 2:
		is_picks_valid = False		
	else:
		is_picks_valid = True	

	return is_picks_valid	

def game_valid(game_week, game_away, game_home):

	game_status = 'True'
	all_games = games.objects.filter(week=game_week)	
		
	for game in all_games:
		current_away = game.away
		current_home = game.home
		if current_away == game_away or current_away == game_home:
			game_status = False
			break
		if current_home == game_home or current_home == game_away:
			game_status = False
			break
	
	return game_status	


def home(request):
	all_picks = picks.objects.all
	return render(request, 'home.html', {'all_picks': all_picks})


def add_picks(request):
	if request.method == "POST":		
		form = picksForm(request.POST or None)
		if form.is_valid():		
			global afce_team, afcn_team, afcs_team, afcw_team, nfce_team, nfcn_team, nfcs_team, nfcw_team
			afce_team = request.POST['afce']
			afcn_team = request.POST['afcn']
			afcs_team = request.POST['afcs']
			afcw_team = request.POST['afcw']
			nfce_team = request.POST['nfce']
			nfcn_team = request.POST['nfcn']
			nfcs_team = request.POST['nfcs']
			nfcw_team = request.POST['nfcw']	
			if picks_valid():
				form.save()
				messages.success(request, ('Picks have been added.'))
				return redirect('add_picks')
			else:
				messages.success(request, ('Invalid set of picks.'))																		
				return redirect('add_picks')
			
		else:
			messages.success(request, ('That set of picks has already been taken.'))	
			return render(request, 'add_picks.html', {})	
	else:
		return render(request, 'add_picks.html', {})			


def calculate(request):
	if request.method == "POST":		
			all_picks = picks.objects.all()
			all_teams = teams.objects.all()
			
			for pick in all_picks:
				playername = pick.name
				afce_points = 0
				afcn_points = 0
				afcs_points = 0
				afcw_points = 0
				nfce_points = 0
				nfcn_points = 0
				nfcs_points = 0
				nfcw_points = 0
				total_points = 0
				afce_team = pick.afce
				afcn_team = pick.afcn
				afcs_team = pick.afcs
				afcw_team = pick.afcw
				nfce_team = pick.nfce 
				nfcn_team = pick.nfcn 
				nfcs_team = pick.nfcs 
				nfcw_team = pick.nfcw 
				record_id = pick.id

				for cur_team in all_teams:
					points = 0
					current_team = cur_team.team
					points = cur_team.points

					if afce_team  == current_team: 
						afce_points = points
						total_points = int(total_points) + int(afce_points)						
						current_record = picks.objects.get(pk=record_id)
						current_record.points = str(total_points)
						current_record.save()
						current_record.afcescore = str(afce_points)
						current_record.save()
					if afcn_team == current_team:
						afcn_points = points
						total_points = int(total_points) + int(afcn_points)						
						current_record = picks.objects.get(pk=record_id)
						current_record.points = str(total_points)
						current_record.save()
						current_record.afcnscore = str(afcn_points)
						current_record.save()
					if afcs_team == current_team:
						afcs_points = points
						total_points = int(total_points) + int(afcs_points)						
						current_record = picks.objects.get(pk=record_id)
						current_record.points = str(total_points)
						current_record.save()
						current_record.afcsscore = str(afcs_points)
						current_record.save()	
					if afcw_team == current_team:
						afcw_points = points
						total_points = int(total_points) + int(afcw_points)						
						current_record = picks.objects.get(pk=record_id)
						current_record.points = str(total_points)
						current_record.save()
						current_record.afcwscore = str(afcw_points)
						current_record.save()	
					if nfce_team == current_team:
						nfce_points = points
						total_points = int(total_points) + int(nfce_points)						
						current_record = picks.objects.get(pk=record_id)
						current_record.points = str(total_points)
						current_record.save()
						current_record.nfcescore = str(nfce_points)
						current_record.save()			
					if nfcn_team == current_team:
						nfcn_points = points
						total_points = int(total_points) + int(nfcn_points)						
						current_record = picks.objects.get(pk=record_id)
						current_record.points = str(total_points)
						current_record.save()
						current_record.nfcnscore = str(nfcn_points)
						current_record.save()	
					if nfcs_team == current_team:
						nfcs_points = points
						total_points = int(total_points) + int(nfcs_points)						
						current_record = picks.objects.get(pk=record_id)
						current_record.points = str(total_points)
						current_record.save()
						current_record.nfcsscore = str(nfcs_points)
						current_record.save()			
					if nfcw_team == current_team:
						nfcw_points = points
						total_points = int(total_points) + int(nfcw_points)						
						current_record = picks.objects.get(pk=record_id)
						current_record.points = str(total_points)
						current_record.save()
						current_record.nfcwscore = str(nfcw_points)
						current_record.save()		
										
			messages.success(request, ('Scores have been generated.'))	

			all_picks = picks.objects.order_by('-points','name')

			return render(request, 'list_stats.html', {
				'all_picks': all_picks
				})		
		
	else:
		return render(request, 'calculate.html', {})


def list_stats(request):
	all_picks = picks.objects.order_by('-points','name')
	return render(request, 'list_stats.html', {'all_picks': all_picks})	


def list_picks(request):
	all_picks = picks.objects.all
	return render(request, 'list_picks.html', {'all_picks': all_picks})		


def edit_picks(request, list_id):
	if request.method == "POST":
		current_pick = picks.objects.get(pk=list_id)
		form = picksForm(request.POST or None, instance=current_pick)
		if form.is_valid():
			global afce_team, afcn_team, afcs_team, afcw_team, nfce_team, nfcn_team, nfcs_team, nfcw_team
			afce_team = request.POST['afce']
			afcn_team = request.POST['afcn']
			afcs_team = request.POST['afcs']
			afcw_team = request.POST['afcw']
			nfce_team = request.POST['nfce']
			nfcn_team = request.POST['nfcn']
			nfcs_team = request.POST['nfcs']
			nfcw_team = request.POST['nfcw']	
			if picks_valid():
				form.save()
				messages.success(request, ('Set of picks has been edited.'))
				return redirect('list_picks')
			else:
				messages.success(request, ('Invalid set of picks.'))																		
				return redirect('list_picks')	
		else:
			messages.success(request, ('That set of picks has already been taken.'))
			all_picks = picks.objects.all
			return render(request, 'list_picks.html', {'all_picks': all_picks})	
	else:
		get_pick = picks.objects.get(pk=list_id)
		return render(request, 'edit_picks.html', {'get_pick': get_pick})


def delete_picks(request, list_id):
	if request.method == "POST":
		current_pick = picks.objects.get(pk=list_id)
		current_pick.delete()
		messages.success(request, ('Set of picks has been deleted.'))
		return redirect('list_picks')
	else:
		messages.success(request, ('Nothing To See Here...'))	
		return redirect('list_picks')


def add_teams(request):
	if request.method == "POST":
		form = teamsForm(request.POST or None)
		if form.is_valid():
			form.save()
			messages.success(request, ('Team has been added.'))
			return redirect('add_teams')
		else:
			messages.success(request, ('That team has already been entered.'))	
			return render(request, 'add_teams.html', {})	
	else:
		return render(request, 'add_teams.html', {})	


def list_teams(request):
	all_teams = teams.objects.order_by('-points','team')
	return render(request, 'list_teams.html', {'all_teams': all_teams})	


def edit_teams(request, list_id):
	if request.method == "POST":
		current_team = teams.objects.get(pk=list_id)
		form = teamsForm(request.POST or None, instance=current_team)
		if form.is_valid():
			form.save()
			messages.success(request, ('Team has been edited.'))
			return redirect('list_teams')
		else:
			messages.success(request, ('Seems like there was an error...'))	
			return render(request, 'edit_teams.html', {})	
	else:
		get_team = teams.objects.get(pk=list_id)
		return render(request, 'edit_teams.html', {'get_team': get_team})


def delete_teams(request, list_id):
	if request.method == "POST":
		current_team = teams.objects.get(pk=list_id)
		current_team.delete()
		messages.success(request, ('Team has been deleted.'))
		return redirect('list_teams')
	else:
		messages.success(request, ('Nothing to see here...'))	
		return redirect('list_teams')	


def add_games(request):
	if request.method == "POST":		
		form = gamesForm(request.POST or None)
		if form.is_valid():		
			global game_week, game_away, game_home
			game_week = request.POST['week']
			game_away = request.POST['away']
			game_home = request.POST['home']	
						
			if game_valid(game_week, game_away, game_home):
				form.save()
				messages.success(request, ('Game has been added.'))
				#return redirect('add_games')
				return render(request, 'add_games.html', {'game_week': game_week})
			else:
				messages.success(request, ('Invalid team used in game.'))																		
				return render(request, 'add_games.html', {'game_week': game_week})
			
		else:
			messages.success(request, ('That game has already been entered or team has already been used.'))	
			return render(request, 'add_games.html', {})	
	else:
		return render(request, 'add_games.html', {})	


def list_games(request):
	all_games = games.objects.order_by('week')
	return render(request, 'list_games.html', {'all_games': all_games})	

'''
def edit_games(request, list_id):
	if request.method == "POST":
		current_game = games.objects.get(pk=list_id)
		form = gamesForm(request.POST or None, instance=current_game)
		if form.is_valid():
			form.save()
			messages.success(request, ('Game has been edited.'))
			return redirect('list_games')
		else:
			messages.success(request, ('Game or Team has already been used.'))	
			return render(request, 'edit_games.html', {})	
	else:
		get_game = games.objects.get(pk=list_id)
		return render(request, 'edit_games.html', {'get_game': get_game})
'''


def edit_games(request, list_id):
	if request.method == "POST":
		current_game = games.objects.get(pk=list_id)
		form = gamesForm(request.POST or None, instance=current_game)
		if form.is_valid():
			global game_week, game_away, game_home
			game_week = request.POST['week']
			game_away = request.POST['away']
			game_home = request.POST['home']	
			if game_valid(game_week, game_away, game_home):
				form.save()
				messages.success(request, ('Game has been edited.'))
				return redirect('list_games')
			else:				
				messages.success(request, ('Invalid team used in game.'))																		
				return redirect('list_games')	
		else:
			messages.success(request, ('Game or Team has already been used.'))	
			return render(request, 'edit_games.html', {})	
	else:
		get_game = games.objects.get(pk=list_id)
		return render(request, 'edit_games.html', {'get_game': get_game})		


def delete_games(request, list_id):
	if request.method == "POST":
		current_game = games.objects.get(pk=list_id)
		current_game.delete()
		messages.success(request, ('Game has been deleted.'))
		return redirect('list_games')
	else:
		messages.success(request, ('Nothing to see here...'))	
		return redirect('list_games')		

def calculate_team(request):
	if request.method == "POST":
		calc_week = request.POST['week']	

		all_games = games.objects.filter(week=calc_week)
		all_teams = teams.objects.all()
			
		for game in all_games:				
			away = game.away
			awayscore = game.awayscore
			home = game.home
			homescore = game.homescore
			awaypoints = 0
			homepoints = 0

			if awayscore > homescore:
				awaypoints = awaypoints + 3
			if awayscore < homescore:
				homepoints = homepoints + 3
			if awayscore == homescore:
				homepoints = homepoints + 1
				awaypoints = awaypoints + 1
			if awayscore >= 42:
				awaypoints = awaypoints + 1
			if homescore >= 42:
				homepoints = homepoints + 1
			if awayscore == 0:
				homepoints = homepoints + 2
			if homescore == 0:
				awaypoints = awaypoints + 2			
					
			for team in all_teams:		
				record_id = team.id
				current_team = str(team.team)	
				total_pts = team.points
				
				if away  == current_team: 			
					total_pts = total_pts + awaypoints
					
					current_record = teams.objects.get(pk=record_id)
					if calc_week == '1':
						current_record.week1 = str(awaypoints)
					if calc_week == '2':
						current_record.week2 = str(awaypoints)
					if calc_week == '3':
						current_record.week3 = str(awaypoints)
					if calc_week == '4':
						current_record.week4 = str(awaypoints)
					if calc_week == '5':
						current_record.week5 = str(awaypoints)
					if calc_week == '6':
						current_record.week6 = str(awaypoints)
					if calc_week == '7':
						current_record.week7 = str(awaypoints)
					if calc_week == '8':
						current_record.week8 = str(awaypoints)
					if calc_week == '9':
						current_record.week9 = str(awaypoints)
					if calc_week == '10':
						current_record.week10 = str(awaypoints)
					if calc_week == '11':
						current_record.week11 = str(awaypoints)					
					if calc_week == '12':
						current_record.week12 = str(awaypoints)
					if calc_week == '13':
						current_record.week13 = str(awaypoints)
					if calc_week == '14':
						current_record.week14 = str(awaypoints)
					if calc_week == '15':
						current_record.week15 = str(awaypoints)
					if calc_week == '16':
						current_record.week16 = str(awaypoints)	
					if calc_week == '17':
						current_record.week17 = str(awaypoints)			
					current_record.points = str(total_pts)
					current_record.save()	
				if home == current_team:			
					total_pts = total_pts + homepoints
					
					current_record = teams.objects.get(pk=record_id)
					if calc_week == '1':
						current_record.week1 = str(homepoints)
					if calc_week == '2':
						current_record.week2 = str(homepoints)
					if calc_week == '3':
						current_record.week3 = str(homepoints)
					if calc_week == '4':
						current_record.week4 = str(homepoints)
					if calc_week == '5':
						current_record.week5 = str(homepoints)
					if calc_week == '6':
						current_record.week6 = str(homepoints)
					if calc_week == '7':
						current_record.week7 = str(homepoints)
					if calc_week == '8':
						current_record.week8 = str(homepoints)
					if calc_week == '9':
						current_record.week9 = str(homepoints)
					if calc_week == '10':
						current_record.week10 = str(homepoints)
					if calc_week == '11':
						current_record.week11 = str(homepoints)					
					if calc_week == '12':
						current_record.week12 = str(homepoints)
					if calc_week == '13':
						current_record.week13 = str(homepoints)
					if calc_week == '14':
						current_record.week14 = str(homepoints)
					if calc_week == '15':
						current_record.week15 = str(homepoints)
					if calc_week == '16':
						current_record.week16 = str(homepoints)	
					if calc_week == '17':
						current_record.week17 = str(homepoints)	
					current_record.points = str(total_pts)
					current_record.save()				

		messages.success(request, ('Scores have been generated.'))	

		all_teams = teams.objects.order_by('-points','team')		

		return render(request, 'list_teams.html', {
			'all_teams': all_teams
			})		
		
	else:
		return render(request, 'calculate_team.html', {})	

							