from django.shortcuts import render, redirect
from .models import UserProfile
from home.models import Product
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


# Create your views here.

def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        mail = request.POST.get("mail")
        phone_number = request.POST.get("phone")

        user = User.objects.create_user(username = username, password = password, email = mail)
        user.save()

        profile = UserProfile.objects.create(user = user, phone_number = phone_number)
        profile.save()

        context = {
            "message" : "User Added Successfully"
        }

        return render(request, "user/register.html", context = context )



    return render(request, "user/register.html")

def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        auth_user = authenticate(request, username = username, password = password)
        all_entries = Product.objects.all()

        context = {
            "message" : "Invalid credentials",
            "all_entries" : all_entries
        }

        if auth_user is not None:
            login(request, auth_user)

            return redirect("/home/")
        else:
            return render(request, "user/login_page.html", context = context)
    return render(request, "user/login_page.html")

def logout_page(request):
    logout(request)

    return redirect("/login/")


