from django.urls import path

from . import views

# map urls with views
urlpatterns = [

    path('', views.index, name='leaveRequest.index'),
    path('<int:id>', views.show, name='leaveRequest.show'),
    path('create', views.create, name='leaveRequest.create'),
    path('update/<int:id>', views.update, name='leaveRequest.update'),
    path('delete/<int:id>', views.delete, name='leaveRequest.delete'),

]
