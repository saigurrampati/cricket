from django.db import models


class Team(models.Model):
    team_id = models.DecimalField(max_digits=2, primary_key=True, decimal_places=0)
    name = models.CharField(max_length=50)
    captain = models.CharField(max_length=50)
    logo_url = models.ImageField(upload_to='')
    state = models.CharField(max_length=5)

    def __str__(self):
        s = str(self.team_id) + "," + str(self.state) + "," + str(self.name) + "," + \
            str(self.captain) + "," + str(self.logo_url)
        return s


class Player(models.Model):
    player_id = models.DecimalField(max_digits=2, primary_key=True, decimal_places=0)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    jersey_id = models.CharField(max_length=100)
    role = models.CharField(max_length=50)
    played = models.IntegerField(max_length=100)
    runs = models.DecimalField(max_digits=5, decimal_places=0)
    max_runs = models.IntegerField(max_length=100)
    fifties = models.IntegerField(max_length=100)
    hundreds = models.IntegerField(max_length=100)
    wickets = models.DecimalField(max_digits=5, decimal_places=0)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='')


    def __str__(self):
        return self.jersey_id


class Match(models.Model):
    match_id = models.DecimalField(max_digits=2, primary_key=True, decimal_places=0)
    date = models.DateField()
    time = models.TimeField()
    team1 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team_one')
    team2 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team_two')
    team1_score = models.CharField(max_length=50, null=True, blank=True)
    team2_score = models.CharField(max_length=50, null=True, blank=True)
    team1_overs = models.CharField(max_length=50, null=True, blank=True)
    team2_overs = models.CharField(max_length=50, null=True, blank=True)
    result = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        s = str(self.date) + "," + str(self.time) + "," + str(self.result)
        return s


class Statistics(models.Model):
    statistics_id = models.DecimalField(max_digits=2, primary_key=True, decimal_places=0)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    played = models.DecimalField(max_digits=5, decimal_places=0)
    won = models.DecimalField(max_digits=5, decimal_places=0)
    lost = models.DecimalField(max_digits=5, decimal_places=0)
    tied = models.DecimalField(max_digits=5, decimal_places=0)
    points = models.DecimalField(max_digits=5, decimal_places=0)

    def __str__(self):
        s = str(self.statistics_id) + "," + str(self.team) + "," + str(self.played) + "," + str(self.won) + "," + str(
            self.lost) + "," + str(self.tied) + "," + str(self.points)
        return s
