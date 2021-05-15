from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Team, Player, Match, Statistics
import datetime
from .form import TeamForm, PlayerForm, MatchForm


def home(request):
    return render(request, 'ipl/home.html', {})


def players(request):
    player = Player.objects.all()
    return render(request, 'ipl/players.html', {'player': player})


def create(request):
    if request.method == "POST":
        print(request.POST)
        form = PlayerForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/ipl/')
    else:
        form = PlayerForm()
        return render(request, 'ipl/create.html', {'form': form})


def details(request, player_id):
    player_detail = Player.objects.get(player_id=player_id)
    return render(request, 'ipl/details.html', {'player_detail': player_detail})


def teams(request):
    if request.method == "POST":
        print(request.POST)
        form = TeamForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/ipl/')
    else:
        form = TeamForm()
        return render(request, 'ipl/teams.html', {'form': form})


def franchise(request):
    team = Team.objects.all()
    return render(request, 'ipl/franchise.html', {'team': team})




def team_details(request, team_id):
    team_detail = Player.objects.get(team_id=team_id)
    player = Player.objects.all()
    return render(request, 'ipl/team_details.html', {'team_detail': team_detail, 'player': player})

