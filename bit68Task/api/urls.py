from django.urls import path, include
from rest_auth.views import (LoginView as RestLogin, LogoutView as RestLogout)
from rest_auth.registration.views import RegisterView
from .views import WeatherAPI
app_name='api'
urlpatterns = [
	#REST_ENDPOINTs
    path('rest-auth/register', RegisterView.as_view(), name='rest_register'),
    path('rest-auth/login/', RestLogin.as_view(), name='rest_login'),
    # path('rest-auth/logout/', RestLogout.as_view(), name='rest_logout'),
    path('api/', WeatherAPI.as_view(), name='weather-api'),
]
