from django.shortcuts import render

# Create your views here.

def cart_views(request):
    return render(request, "cart/cart_view.html")