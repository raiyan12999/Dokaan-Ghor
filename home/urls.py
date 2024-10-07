from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name = "index"),
    path("form/", views.form, name = "form"),
    path("product/<int:pk>/", views.product, name = "product"),
    path("cart/<int:pk>/", views.cart, name = "cart"),
    path("sold/<int:pk>/", views.sold, name = "sold")
]
