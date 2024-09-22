from django.db import models

# Create your models here.

class Team(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='team_logos', blank=True)
    founded = models.DateField()
    stadium = models.CharField(max_length=100)
    manager = models.CharField(max_length=100)
    captain = models.CharField(max_length=100)
    description = models.TextField(help_text='A brief description of the team and its history')
    website = models.URLField()

    class Meta:
        verbose_name_plural = 'Teams'


    def __str__(self):
        return f"{self.name}  - {self.stadium} - {self.manager}"


TEAM_CATEGORY_CHOICES = (
    ('U21', 'Under-21S'),
    ('U17', 'Under-17S'),
    ('U18', 'Under-18S'),
    ('LEGENDS', 'LEGENDS'),
    ('Team', 'Team'),
)
class TeamCategory(models.Model):
    name = models.ForeignKey(Team, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Team Categories'

    def __str__(self):
        return f"{self.name} - {self.category}"


