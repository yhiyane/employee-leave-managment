from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'LEAVE'
urlpatterns = [
    path('', views.index_leave, name='index_leave'),
    path('requestList', views.request_list, name='request_list'),
    path('cancel_request/<id>', views.cancel_request, name='cancel_request'),
    path('update_request/<id>', views.update_request, name='update_request'),

]
