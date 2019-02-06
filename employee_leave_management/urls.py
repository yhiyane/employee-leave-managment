
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from  akTeams.route import route
urlpatterns = [
    path('home/', include('akTeams.utls.dashboardurl')),
    path('LeaveRequest/', include('akTeams.utls.LeaveRqtUrls')),
    path('leaveType/', include('akTeams.utls.LeaveTypeUrls')),
    path('affectation/', include('akTeams.utls.membreTeamUrls')),
    path('employees/', include('akTeams.utls.empUrls')),
    path('be/', include('akTeams.utls.beUrls')),
    path('position/', include('akTeams.utls.urls')),
    path('team/', include('akTeams.urls')),
    path('', auth_views.LoginView.as_view(template_name='employees/login.html'),name ='login'),
    path('', auth_views.LogoutView.as_view(),name ='logout'),
    # path('', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('api/', include(route.urls)),
    # path('api/', include('akTeams.route')),
]
