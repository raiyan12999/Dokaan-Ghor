from django.db import models
from cart.models import CartItem

# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length = 50)
    price = models.IntegerField(default=50)
    product_image = models.ImageField(upload_to = 'product_image/', blank=True, null=True)
    seller_name = models.CharField(max_length = 50)
    cart = models.ForeignKey(CartItem, on_delete=models.CASCADE, null = True)

    def __str__(self):
        return self.product_name