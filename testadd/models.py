from django.db import models

class picks(models.Model):
	name = models.CharField(max_length=100)
	email = models.EmailField(max_length=75)
	afce = models.CharField(max_length=20, default=None)
	afcescore = models.IntegerField(default=0, blank=True, null=True)
	afcn = models.CharField(max_length=20, default=None)
	afcnscore = models.IntegerField(default=0, blank=True, null=True)
	afcs = models.CharField(max_length=20, default=None)
	afcsscore = models.IntegerField(default=0, blank=True, null=True)
	afcw = models.CharField(max_length=20, default=None)
	afcwscore = models.IntegerField(default=0, blank=True, null=True)
	nfce = models.CharField(max_length=20, default=None)
	nfcescore = models.IntegerField(default=0, blank=True, null=True)
	nfcn = models.CharField(max_length=20, default=None)
	nfcnscore = models.IntegerField(default=0, blank=True, null=True)
	nfcs = models.CharField(max_length=20, default=None)
	nfcsscore = models.IntegerField(default=0, blank=True, null=True)
	nfcw = models.CharField(max_length=20, default=None)
	nfcwscore = models.IntegerField(default=0, blank=True, null=True)
	points = models.IntegerField(default=0, blank=True, null=True)

	class Meta:
		constraints = [
		models.UniqueConstraint(fields=['afce', 'afcn', 'afcs', 'afcw', 'nfce', 'nfcn', 'nfcs', 'nfcw'], name='unique_picks')]
		verbose_name_plural = "picks"	

	def __str__(self):
		return self.name + " | " +  self.afce + " | " + self.afcn + " | " +  self.afcs + " | " + self.afcw + " | " + self.nfce + " | " + self.nfcn + " | " + self.nfcs + " | " + self.nfcw

class teams(models.Model):
	team = models.CharField(max_length=20)
	division = models.CharField(max_length=4)
	status = models.CharField(max_length=2)
	week1 = models.IntegerField(default=0, blank=True, null=True)
	week2 = models.IntegerField(default=0, blank=True, null=True)
	week3 = models.IntegerField(default=0, blank=True, null=True)
	week4 = models.IntegerField(default=0, blank=True, null=True)
	week5 = models.IntegerField(default=0, blank=True, null=True)
	week6 = models.IntegerField(default=0, blank=True, null=True)
	week7 = models.IntegerField(default=0, blank=True, null=True)
	week8 = models.IntegerField(default=0, blank=True, null=True)
	week9 = models.IntegerField(default=0, blank=True, null=True)
	week10 = models.IntegerField(default=0, blank=True, null=True)
	week11 = models.IntegerField(default=0, blank=True, null=True)
	week12 = models.IntegerField(default=0, blank=True, null=True)
	week13 = models.IntegerField(default=0, blank=True, null=True)
	week14 = models.IntegerField(default=0, blank=True, null=True)
	week15 = models.IntegerField(default=0, blank=True, null=True)
	week16 = models.IntegerField(default=0, blank=True, null=True)
	week17 = models.IntegerField(default=0, blank=True, null=True)
	points = models.IntegerField(default=0, blank=True, null=True)

	class Meta:
		constraints = [
		models.UniqueConstraint(fields=['team'], name='unique_teams')]
		verbose_name_plural = "teams"	

	def __str__(self):
		return self.team + " | " + self.division + " | " + self.status

class games(models.Model):
	week = models.IntegerField(default=0, blank=True, null=True)
	away = models.CharField(max_length=20)
	awayscore = models.IntegerField(default=0, blank=True, null=True)
	home = models.CharField(max_length=20)
	homescore = models.IntegerField(default=0, blank=True, null=True)
	
	class Meta:				
		verbose_name_plural = "games"	

	def __str__(self):
		return str(self.week) + " | " + self.away + " | " + self.home	
