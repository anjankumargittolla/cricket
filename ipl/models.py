from django.db import models


# Create your models here.


class Team(models.Model):
    team_id = models.IntegerField(unique=True)
    team_name = models.CharField(max_length=25)
    team_logo = models.FileField(upload_to='media/', null=True, blank=True)
    club_state = models.CharField(max_length=15)

    def __str__(self):
        return str(self.team_name)


class Player(models.Model):
    player_id = models.IntegerField(unique=True)
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    player_image = models.ImageField('media/')
    jersey_number = models.IntegerField()
    ipl_team = models.ForeignKey(Team, on_delete=models.CASCADE)
    matches = models.IntegerField()
    runs = models.IntegerField()
    highest = models.IntegerField()
    half_centuries = models.IntegerField()
    centuries = models.IntegerField()


class Match(models.Model):
    team1 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team_one')
    team2 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team_two')
    result = models.ForeignKey(Team, max_length=50, null=True, blank=True, on_delete=models.CASCADE)

    # def __str__(self):
    #     return str(self.result)


class Points(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    played = models.IntegerField(default=0)
    won = models.IntegerField(default=0)
    lost = models.IntegerField(default=0)
    points = models.IntegerField(default=0)

    def __str__(self):
        return str(self.team)
