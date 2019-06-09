from django.shortcuts import render, redirect
from menu.models import Pizza
from . models import Cart

def cart_home(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    return render(request, 'order/cart.html')

def cart_update(request):
    product_id= 1
    product_obj = Pizza.objects.get(id=1)
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    cart_obj.products.add(product_obj)

    return redirect('/cart')
