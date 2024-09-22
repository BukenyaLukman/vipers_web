from django.db import models

# Create your models here.


class Tournament(models.Model):
    tournament_name = models.CharField(max_length=100)
    tournament_sponsor = models.CharField(max_length=100)


    def __str__(self):
        return self.tournament_name
