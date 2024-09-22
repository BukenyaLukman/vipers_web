from django.db import models
from teams.models import Team

# Players model


FOOT_CHOICES = (
    ('Right', 'Right'),
    ('Left', 'Left'),
    ('Both', 'Both'),
)
PLAYER_POSITIONS = (
    ('Goalkeeper', 'Goalkeeper'),
    ('Defender', 'Defender'),
    ('Midfielder', 'Midfielder'),
    ('Forward', 'Forward'),
)
class Player(models.Model):
    name = models.CharField(max_length=200)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, null=True, blank=True)
    nationality = models.CharField(max_length=200)
    age = models.IntegerField()
    height = models.IntegerField()
    date_of_birth = models.DateField()
    height = models.IntegerField()
    weight = models.IntegerField()
    position = models.CharField(max_length=200, choices=PLAYER_POSITIONS)
    jersey_number = models.IntegerField()
    foot = models.CharField(max_length=200, choices=FOOT_CHOICES)
    club = models.CharField(max_length=200, null=True, blank=True, default='Vipers SC')
    transfer_value = models.IntegerField(null=True, blank=True, default=0)
    image = models.ImageField(null=True, blank=True)
    awards = models.TextField(null=True, blank=True)


    class Meta:
        verbose_name_plural = 'Player'



    def __str__(self):
        return str(f"{self.name} -- {self.position} - {self.jersey_number}")

class PlayerStatistics(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    matches_played = models.IntegerField()
    goals = models.IntegerField()
    assists = models.IntegerField()
    yellow_cards = models.IntegerField()
    red_cards = models.IntegerField()

    class Meta:
        verbose_name_plural = 'Player Statistics'

    def __str__(self):
        return str(f"{self.player} - {self.matches_played} - {self.goals} - {self.assists} - {self.yellow_cards} - {self.red_cards}")