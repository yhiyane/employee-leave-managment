from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'CRUD_APP'
urlpatterns = [
    path('', views.home, name='employee_home'),
    path('delete_emp/<id>', views.delete_employee, name='delete_emp'),
    path('add_emp/', views.add_emp, name='add_emp'),
    path('update_emp/<id>', views.update_emp, name='update_emp'),
    path('team_index/', views.team_index, name='team_index'),
    path('add_team/', views.add_team, name='add_team'),
    path('team_index/delete_team/<id>', views.delete_team, name='delete_team'),
    path('team_index/update_team/<id>', views.update_team, name='update_team'),
    path('position_index/', views.position_index, name='position_index'),
    path('add_position/', views.add_position, name='add_position'),
    path('position_index/delete_position/<id>', views.delete_position, name='delete_position'),
    path('position_index/update_position/<id>', views.update_position, name='update_position'),
    path('be_index/', views.be_index, name='be_index'),
    path('add_be/', views.add_be, name='add_be'),
    path('be_index/delete_be/<id>', views.delete_be, name='delete_be'),
    path('be_index/update_be/<id>', views.update_be, name='update_be'),
    path('leave_index/', views.leave_index, name='leave_index'),
    path('leave_request/', views.leave_request, name='leave_request'),
    path('leave_index/delete_req/<id>', views.delete_leave_request, name='delete_req'),
    path('leave_index/update_req/<id>', views.update_leave_request, name='update_req'),

]