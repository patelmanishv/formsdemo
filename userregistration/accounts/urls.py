# accounts/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('registration_success/', views.registration_success, name='registration_success'),
    # Add more URL patterns if needed
]
