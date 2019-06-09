from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.menupage, name='menu-home'),
    path('about/', views.about, name='menu-about'),
    path('pizza/', views.pizza, name='menu-pizza'),
    path('drinks/', views.drinks, name='menu-pizza'),
    path('signup/', include('accounts.urls')),
]
