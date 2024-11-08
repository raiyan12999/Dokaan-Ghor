from django.urls import path
from . import views

urlpatterns = [
    path("", views.cart_views, name = "cart_view")
]