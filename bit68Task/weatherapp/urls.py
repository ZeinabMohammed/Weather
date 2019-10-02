from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView , LogoutView 
from .views import register, weather
app_name='weatherapp'
urlpatterns = [
    # HTML AUTH
    path('register/', register, name='register'),
    path('login/', LoginView.as_view(template_name='login.html') , name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html') , name='logout'),
    #WEATHER
    path('', weather, name='weather-form'),
]
