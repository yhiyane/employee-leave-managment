from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'CRUD'
urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<id>', views.delete, name='delete'),
    path('create', views.create, name='create'),
    path('add_newEmployer', views.add_newEmployer, name='add_newEmployer'),
    path('edit/<id>', views.edit, name='edit'),
    path('teams', views.teams, name='teams'),
    path('delete_team/<id>', views.delete_team, name='delete_team'),
    path('register/<id>', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('add_teams', views.add_teams, name='add_teams'),
    path('find_team/<id>', views.find_team, name='find_team'),
    path('edit_team/<id>', views.edit_team, name='edit_team'),
    path('bu', views.bu, name='bu'),
    path('add_bu', views.add_bu, name='add_bu'),
    path('edit_bu/<id>', views.edit_bu, name='edit_bu'),
    path('find_bu/<id>', views.find_bu, name='find_bu'),
    path('delete_bu/<id>', views.delete_bu, name='delete_bu'),
    path('position', views.position, name='position'),
    path('add_position', views.add_position, name='add_position'),
    path('edit_position/<id>', views.edit_position, name='edit_position'),
    path('find_position/<id>', views.find_position, name='find_position'),
    path('delete_position/<id>', views.delete_position, name='delete_position'),
]