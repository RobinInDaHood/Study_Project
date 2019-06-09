from django.db import models

class Merch(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(default='')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(default='/images/shop/placeholder.png', upload_to='images/shop')

    def __str__(self):
        return self.name
