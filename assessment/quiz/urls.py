# main/urls.py
from django.urls import path
from .views import RegisterView, LoginView, ProfileView, home
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [

    path('', home, name='home'),
    path('api/accounts/signup/', RegisterView.as_view(), name='signup'),
    path('api/accounts/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # login
    path('api/accounts/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/accounts/profile/', ProfileView.as_view(), name='profile'),


]
