
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from . import views
from users import views as user_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('leave/', include('leaveManagmentItazouti.urls')),
    path('accounts/',include('django.contrib.auth.urls')),
    path('register/<id>', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name= 'users/logout.html'), name='logout'),
    path('profile/', user_views.profile, name='profile'),
    path('change_password/', user_views.change_password, name='change_password'),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



