from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'LEAVE'
urlpatterns = [
    path('', views.index_leave, name='index_leave'),
    path('requestList', views.request_list, name='request_list'),
    path('employers_requests/<id>', views.employers_requests, name='employers_requests'),
    path('cancel_request/<id>', views.cancel_request, name='cancel_request'),
    path('update_request/<id>', views.update_request, name='update_request'),
    path('show_notification_manager/<id>', views.show_notification_manager, name='show_notification_manager'),
    path('update_employer_request/<id>', views.update_employer_request, name='update_employer_request'),
    path('delete_employer_request/<id>', views.delete_employer_request, name='delete_employer_request')

]
