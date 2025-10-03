from django.urls import path
from django.contrib import admin

from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('home/', views.home, name='home'),
    path('student-login/', views.sign, name='student-login'),
    path('profile/', views.profile, name='profile'),
    path('facilities/', views.facilities, name='facilities'),
    path('complaints/', views.complaints, name='complaints'),
    path('rules/', views.rules, name='rules'),
    path('contact/', views.contact, name='contact'),
    path('reset/',views.reset,name = 'reset')

]
    
