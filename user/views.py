from django.shortcuts import render
from .models import UserProfile
from django.contrib.auth.models import User


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


