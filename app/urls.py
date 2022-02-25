from knox import views as knox_views
from .views import LoginAPI, RegisterAPI, UserAPI, ChangePasswordView
from django.urls import path

urlpatterns = [
    path('api/auth/register/', RegisterAPI.as_view(), name='register'),
    path('api/auth/login/', LoginAPI.as_view(), name='login'),
    path('api/auth/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/auth/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('api/auth/user/', UserAPI.as_view(), name='user'),
    path('api/auth/change-password/', ChangePasswordView.as_view(), name='change-password'),
]