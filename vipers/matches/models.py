from django.db import models
from teams.models import Team



class Match(models.Model):
    """
    Model for a match
    """
    home_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='home_team')
    away_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='away_team')
    date = models.DateTimeField()
    home_team_logo = models.ImageField(upload_to='team_logos', null=True, blank=True)
    away_team_logo = models.ImageField(upload_to='team_logos', null=True, blank=True)
    stadium = models.CharField(max_length=200)
    match_time = models.TimeField(blank=True, null=True)
    competion = models.ForeignKey('Competition', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Matches'
    

    def __str__(self):
        return f'{self.home_team} vs {self.away_team}'


class Competition(models.Model):
    name = models.CharField(max_length=200)
    competion_logo = models.ImageField(upload_to='competion_logos')
    description = models.TextField(help_text='A brief description of the competion and its history')
    sponsor = models.CharField(max_length=200)


    def __str__(self):
        return f"{self.name} - {self.sponsor}"



class MatchResult(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    home_team_score = models.IntegerField()
    away_team_score = models.IntegerField()

    def __str__(self):
        return f"{self.match} - {self.home_team_score} - {self.away_team_score}"

    