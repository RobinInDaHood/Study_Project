from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.cart_home, name='cart'),
    path('cart/', views.cart_home, name='cart-home'),
    path('update/', views.cart_update, name='cart-update')
]
