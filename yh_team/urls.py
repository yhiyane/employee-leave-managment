from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='team.index'),
    path('<int:id>', views.show, name='team.show'),
    path('create', views.create, name='team.create'),
    path('update/<int:id>', views.update, name='team.update'),
    path('delete/<int:id>', views.delete, name='team.delete'),
]
