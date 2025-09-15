from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='app_principal/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='app_principal/login.html'), name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('crear_candidato/', views.crear_candidato, name='crear_candidato'),
    path('examen/', views.presentar_examen, name='examen'),
]
