from django.urls import path
from . import views

urlpatterns = [
        path('', views.index, name='index'),
        path('stima-score/', views.stimaScore, name='stima-score'),
        path('stima-tarro/', views.stimaTarro, name='stima-tarro'),
        path('stima-cash/', views.stimaCash, name='stima-cash')
        #path('game/<int:id>', views.game, name='game')
        ]