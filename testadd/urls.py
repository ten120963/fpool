from django.urls import path
from . import views
from .views import SearchResultsView

urlpatterns = [
	path('', views.home, name="home"),
	path('add_picks', views.add_picks, name="add_picks"),  
	path('calculate', views.calculate, name="calculate"),
	path('list_stats', views.list_stats, name="list_stats"),
	path('list_picks', views.list_picks, name="list_picks"),
	path('edit_picks/<list_id>', views.edit_picks, name="edit_picks"),   
	path('delete_picks/<list_id>', views.delete_picks, name="delete_picks"), 	
	path('add_teams', views.add_teams, name="add_teams"), 
	path('list_teams', views.list_teams, name="list_teams"), 
	path('edit_teams/<list_id>', views.edit_teams, name="edit_teams"),   
	path('delete_teams/<list_id>', views.delete_teams, name="delete_teams"), 
	path('add_games', views.add_games, name="add_games"), 
	path('list_games', views.list_games, name="list_games"), 
	path('edit_games/<list_id>', views.edit_games, name="edit_games"),  
	path('delete_games/<list_id>', views.delete_games, name="delete_games"), 
	path('calculate_team', views.calculate_team, name="calculate_team"),	
	path('search/', SearchResultsView.as_view(), name='search_results'),    
]

