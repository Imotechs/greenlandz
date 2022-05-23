
from django.contrib import admin
from django.urls import path,include, reverse_lazy
from django.contrib.auth import views as auth_views

from django.contrib.auth.views import LoginView,LogoutView
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', LoginView.as_view(template_name = 'dashboard/login.html'), name = 'login'),
    path('accounts/logout/', LogoutView.as_view(template_name = 'mainapp/logout.html'), name = 'logout'),
    path('', include('mainapp.urls')),
    path('dashboard/', include('dashboard.urls')),

    path('password-reset/', 
        auth_views.PasswordResetView.as_view(
            success_url = reverse_lazy('password_reset_done'),
            template_name = 'mainapp/password_reset.html'),
            name = 'password_reset'),

    path('password-reset-done/', 
        auth_views.PasswordResetDoneView.as_view(template_name = 'mainapp/password_reset_done.html'),name = 'password_reset_done'),
    
    path('password-reset-confirm/<uidb64>/<token>/', 
        auth_views.PasswordResetConfirmView.as_view(
            success_url = reverse_lazy('password_reset_complete'),
            template_name = 'mainapp/password_reset_confirm.html'),
            name = 'password_reset_confirm'),
    
    path('password_reset_complete/', 
        auth_views.PasswordResetCompleteView.as_view( template_name = 'mainapp/password_reset_complete.html'), name = 'password_reset_complete'),


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)