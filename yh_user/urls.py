
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='user.index'),
    path('<int:id>', views.show, name='user.show'),
    path('create', views.create, name='user.create'),
    path('update/<int:id>', views.update, name='user.update'),
    path('delete/<int:id>', views.delete, name='user.delete'),
]
