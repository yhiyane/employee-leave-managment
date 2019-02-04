from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
                  path('admin/', admin.site.urls),
                  path('setting/', include('settingEmployer.urls')),
                  path('leave/', include('leaveRequests.urls')),
                  path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
                  path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),

              ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
