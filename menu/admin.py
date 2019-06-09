from django.contrib import admin
from . models import Pizza, Category, Drinks

# Register your models here.
admin.site.register(Category)
admin.site.register(Pizza)
admin.site.register(Drinks)
