from django.contrib import admin
from django.urls import path, include
from yh_user import views

urlpatterns = [
    path('', include('yh_panel.urls')),
    path('admin/', admin.site.urls),
    path('youssef_hiyane', include('yh_user.urls')),
    path('youssef_hiyane/employee/', include('yh_employee.urls')),
    path('youssef_hiyane/user/', include('yh_user.urls')),
    path('youssef_hiyane/team/', include('yh_team.urls')),
    path('youssef_hiyane/be/', include('yh_be.urls')),
    path('youssef_hiyane/leaveRequest/', include('yh_leaveRequest.urls')),
    path('', include('django.contrib.auth.urls')),

]
