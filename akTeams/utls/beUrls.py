from django.urls import path

from akTeams.view import beView



# map urls with views
urlpatterns = [
    #  business entity
    path('', beView.index, name='be.index'),
    path('create', beView.create, name='be.create'),
    path('update/<int:id>', beView.update, name='be.update'),
    path('delete/<int:id>', beView.delete, name='be.delete'),




]