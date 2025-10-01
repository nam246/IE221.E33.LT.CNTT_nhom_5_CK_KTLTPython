from django.urls import path
from auth_api import views

urlpatterns = [
    path('login/', views.api_login, name='login_api'),
    path('logout/', views.api_logout, name='logout_api'),
]
