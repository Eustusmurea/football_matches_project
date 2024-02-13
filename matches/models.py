from django.db import models

class Match(models.Model):
    home_team = models.CharField(max_length=100)
    away_team = models.CharField(max_length=100)
    competition = models.CharField(max_length=100)
    match_date = models.DateTimeField()

    def __str__(self):
        return f"{self.home_team} vs {self.away_team}"