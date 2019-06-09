from django.shortcuts import render
from .models import Merch

def merch(request):
    merch = Merch.objects.all().order_by('name')
    return render(request, 'shop/shop.html', {'merch' : merch})
