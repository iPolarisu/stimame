from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection
from collections import namedtuple
from .models import Steamapp

# Create your views here
def index(request):
    return render(request, 'stima/index.html')

def stimaScore(request):
    if request.method == "POST":
        score = request.POST['score']
        games = Steamapp.objects.filter(name__unaccent__icontains=score)
        return render(request, 'stima/stima-score.html', {'games':games})
    else:
        return render(request, 'stima/stima-score.html')

def game(request, id):
    game = Steamapp.objects.get(appid=id)
    context = {
        "game": game,
    }
    return render(request, 'stima/game.html', context)

