from django.db import models

# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length = 50)
    price = models.IntegerField(default=50)
    seller_name = models.CharField(max_length = 50)

