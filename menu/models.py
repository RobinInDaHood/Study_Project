from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=20, db_index=True)
    slug = models.SlugField(max_length=20, db_index=True, unique=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Pizza(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=30, db_index=True)
    #topping
    description = models.TextField(default='PizzaSauce')

    price = models.DecimalField(max_digits=4, decimal_places=2)
    available = models.BooleanField(default=True)
    new = models.BooleanField(default=False)
    image = models.ImageField(default='/images/pizza/placeholder.png', upload_to='images/pizza')

    class Meta:
        index_together = (('id', 'slug'))


    def __str__(self):
        return self.name

class Drinks(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=30, db_index=True)
    description = models.TextField(default='1000 Liter')

    price = models.DecimalField(max_digits=4, decimal_places=2)
    available = models.BooleanField(default=True)
    image = models.ImageField(default='/images/drinks/placeholder_soda.png', upload_to='images/drinks')

    class Meta:
        index_together = (('id', 'slug'))

    def __str__(self):
        return self.name
