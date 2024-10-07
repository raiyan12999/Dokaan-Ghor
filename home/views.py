from django.shortcuts import render
from django.http import HttpResponse
from . models import Product

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
        seller_name = request.POST.get("seller_name")

        entry = Product.objects.create(product_name = product_name, price = price, seller_name = seller_name)
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
    context = {
        "current_product" : current_product
    }
    return render(request, "home/cart.html", context)

def sold(request, pk):

    sold_product = Product.objects.get(id = pk)
    sold_product.delete()

    context = {
        "message" : "Item Bought Successfully!"
    }

    return render(request, "home/sold.html", context)

