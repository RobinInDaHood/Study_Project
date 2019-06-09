from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.signup, name='account-home'),
    path('signup/', views.signup, name='account-signup'),
    path('success/', views.success, name='account-success'),
]
