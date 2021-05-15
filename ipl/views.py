from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Team, Player, Match, Statistics
import datetime
from . form import TeamForm, PlayerForm, MatchForm

def players(request):
    player = PlayerForm.objects.all()
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
        return render(request, 'ipl/create.html', {'form': form })



