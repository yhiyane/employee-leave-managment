from django.urls import path

from akTeams.view import membreTeamView



# map urls with views
urlpatterns = [
    #  membre team
    path('create', membreTeamView.create, name='membreTeam.create'),
    path('ajax/load_membres/', membreTeamView.load_membres, name='load_membres'),





]