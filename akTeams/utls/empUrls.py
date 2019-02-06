from django.urls import path

from akTeams.view import empView



# map urls with views
urlpatterns = [
    #  employee
    path('', empView.index, name='emp.index'),
    path('create', empView.create, name='emp.create'),
    path('update/<int:id>', empView.update, name='emp.update'),
    path('delete/<int:id>', empView.delete, name='emp.delete'),
    path('createUser', empView.createUser, name='emp.createUser'),




]