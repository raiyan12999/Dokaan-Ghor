from django.shortcuts import render
from user.models import UserProfile
from cart.models import CartItem
from home.models import Product

# Create your views here.

def cart_views(request):
    if request.user.is_authenticated:
        current_user = request.user
        current_user_profile = UserProfile.objects.get(user = current_user)
        cart_item, created =  CartItem.objects.get_or_create(profile = current_user_profile)
        products = Product.objects.filter(cart = cart_item)

        context = {
            "products" : products,
            "username" : current_user.username,
            "first_name" : current_user.first_name,
            "last_name" : current_user.last_name
        }
    return render(request, "cart/cart_view.html", context)