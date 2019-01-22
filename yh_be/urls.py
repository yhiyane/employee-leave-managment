from django.urls import path
from . import views

# map urls with views
urlpatterns = [
    path('', views.index, name='be.index'),
    path('<int:id>', views.show, name='be.show'),
    path('create', views.create, name='be.create'),
    path('update/<int:id>', views.update, name='be.update'),
    path('delete/<int:id>', views.delete, name='be.delete'),
]
