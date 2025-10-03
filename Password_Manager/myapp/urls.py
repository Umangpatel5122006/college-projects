
# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.home, name='home'),
#     path('add/',views.add_credential, name='add_credential'),
#     path('thank-you/', views.thank_you, name='thank-you'),
#     path('search/', views.search_credential, name='search')
# ]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_credential, name='add_credential'),
    path('thank-you/', views.thank_you, name='thank-you'),
    path('search/', views.search_credential, name='search'),
    path('signup/', views.signup, name='signup'),  # Sign Up
    path('login/', views.login_view, name='login'),  # Login
    path('logout/', views.logout_view, name='logout'),
    path('delete/<int:credential_id>/', views.delete_credential, name='delete_credential'),  # Delete Credential
]

