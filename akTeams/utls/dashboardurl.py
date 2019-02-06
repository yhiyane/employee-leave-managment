from django.urls import path

from akTeams.view import empView



# map urls with views
urlpatterns = [
    #  business entity
    path('', empView.dashboard, name='dashboard'),





]