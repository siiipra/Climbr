# main/urls.py
from django.urls import path
from .views import RegisterView, LoginView, home


urlpatterns = [

    path('', home, name='home'),
    path('api/accounts/signup/', RegisterView.as_view(), name='signup'),
    path('api/accounts/login/', LoginView.as_view(), name='login'),

    #path('', views.home, name='home'),
    #path('signup/', RegisterView.as_view(), name='signup'),
    #path('login/', LoginView.as_view(), name='login'),
]
