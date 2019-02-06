from django.urls import path

from . import views



# map urls with views
urlpatterns = [
    # Team
    path('', views.index, name='team.index'),
    path('create', views.create, name='team.create'),
    path('update/<int:id>', views.update, name='team.update'),
    path('delete/<int:id>', views.delete, name='team.delete'),
    path('affectation/<int:id>', views.affectation, name='team.affectation'),



]