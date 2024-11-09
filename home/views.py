from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . models import Product
from user.models import UserProfile
from cart.models import CartItem

# Create your views here.

def index(request):
    all_entries = Product.objects.all()
    context = {
        "all_entries" : all_entries
    }
    return render(request, "home/index.html", context)

def form(request):
    if request.method == "POST":
        product_name = request.POST.get("product_name")
        price = request.POST.get("price")
        product_image = request.FILES.get("product_image")
        seller_name = request.POST.get("seller_name")

        entry = Product.objects.create(product_name = product_name, price = price, product_image = product_image,seller_name = seller_name)
        entry.save()
        
        

        message = "Proudct Added Successfully"

        context = {
            "message" : message
        }

        return render(request, "home/form.html", context)

    
    return render(request, "home/form.html")


def product(request, pk):
    current_product = Product.objects.get(id = pk)
    context = {
        "pk" : pk,
        "current_product" : current_product
    }
    return render(request, "home/details.html", context)


def cart(request, pk):

    current_product = Product.objects.get(id = pk)

    if request.user.is_authenticated:
        logged_user = request.user
        current_user = UserProfile.objects.get(user = logged_user)
        

        cart_item, created = CartItem.objects.get_or_create(profile = current_user)

        current_product.cart = cart_item
        current_product.save()

        context = {
            "current_product" : current_product,
            "cart_name" : current_product.cart
        }

        return render(request, "home/cart.html", context)
    context = {
        "current_product" : current_product,
        "message" : "User is not logged in"
    }
    return render(request, "home/cart.html", context)

def sold(request, pk):

    sold_product = Product.objects.get(id = pk)
    sold_product.delete()

    context = {
        "message" : "Item Bought Successfully!"
    }

    return render(request, "home/sold.html", context)


