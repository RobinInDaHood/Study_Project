from django.shortcuts import render
from . models import Category, Pizza, Drinks

# Create your views here.

def menupage(request):
    category = None
    categories = Category.objects.all().order_by('id')

    return render(request, 'menu/menupage.html', {'category' : category,
                                                  'categories' : categories})

def pizza(request):
    category = None
    categories = Category.objects.all().order_by('id')
    pizza = Pizza.objects.all().order_by('name')

    return render(request, 'menu/pizza.html', {'category' : category,
                                                  'categories' : categories,
                                                  'pizza' : pizza})

def drinks(request):
    category = None
    categories = Category.objects.all().order_by('id')
    drinks = Drinks.objects.all().order_by('name')

    return render(request, 'menu/drinks.html', {'category' : category,
                                                  'categories' : categories,
                                                  'drinks' : drinks})




def home(request):
    return render(request, 'frontpage/frontpage.html', {'title' : 'Home'})

def about(request):
    return render(request, 'frontpage/about.html',  {'title' : 'About'})
