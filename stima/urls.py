from django.urls import path
from . import views

urlpatterns = [
        path('', views.index, name='index'),
        path('stima-score/', views.stimaScore, name='stima-score'),
        path('game/<int:id>', views.game, name='game')
        ]