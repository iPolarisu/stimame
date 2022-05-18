from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection
from collections import namedtuple

# Create your views here
def index(request):
    return render(request, 'stima/index.html')

def stimaScore(request):
    return render(request, 'stima/stima-score.html')

def stimaTarro(request):
    return render(request, 'stima/stima-tarro.html')

def stimaCash(request):
    return render(request, 'stima/stima-cash.html')

# def game(request, id):
    #game = Steamapp.objects.get(appid=id)
    #media = Media.objects.get(steamapp_id=id)
    #description = Description.objects.get(steamapp_id=id)
    #requirements = Requirements.objects.get(steamapp_id=id)
    #support = Support.objects.filter(steamapp_id=id).first()
    #context = {
    #    "game": game,
    #    "media": media,
    #    "description": description,
    #    "requirements": requirements,
    #    "support": support
    #}
    #return render(request, 'stima/game.html', context)
