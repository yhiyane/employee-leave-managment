from django.urls import path

from akTeams.view import positionView



# map urls with views
urlpatterns = [
    # Position
    path('', positionView.index, name='position.index'),
    path('create', positionView.create, name='position.create'),
    path('update/<int:id>', positionView.update, name='position.update'),
    path('delete/<int:id>', positionView.delete, name='position.delete'),




]