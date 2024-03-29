from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save, post_save, m2m_changed
from menu.models import Pizza, Drinks


User = settings.AUTH_USER_MODEL

class CartManager(models.Manager):
    def new_or_get(self, request):
        cart_id = request.session.get('cart_id', None)
        qs = self.get_queryset().filter(id=cart_id)
        if qs.count() == 1:
            new_obj = False
            print('Cart ID already exists')
            print('Cart ID:', cart_id)
            cart_obj = qs.first()
            if request.user.is_authenticated and cart_obj.user is None:
                cart_obj.user = request.user
                cart_obj.save()

        else:
            cart_obj = self.new(user=request.user)
            request.session['cart_id'] = cart_obj.id
            new_obj = True
        return cart_obj, new_obj

    def new(self, user=None):
        print(user)
        user_obj = None
        if user is not None:
            if user.is_authenticated:
                user_obj = user
        return self.model.objects.create(user=user_obj)


class Cart(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    products = models.ManyToManyField(Pizza, blank=True)
    total = models.DecimalField(default=0, max_digits=6, decimal_places=2)

    objects = CartManager()

    def __str__(self):
        return str(self.id)

def pre_save_cart_reciever(sender, instance, action, *args, **kwargs):
    products = instance.products.all()
    total = 0
    for x in products:
        print(products)
        total += x.price
    instance.total = total
    instance.save()

m2m_changed.connect(pre_save_cart_reciever, sender=Cart.products.through)
