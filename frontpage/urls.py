from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='frontpage-about'),
    path('menu/', include('menu.urls')),
    path('signup/', include('accounts.urls')),
]
