from django.db import models
from user.models import UserProfile

# Create your models here.

class CartItem(models.Model):
    profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.profile.user.username}'s cart"