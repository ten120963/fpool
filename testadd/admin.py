from django.contrib import admin
from .models import picks, teams, games

admin.site.register(picks)
admin.site.register(teams)
admin.site.register(games)
