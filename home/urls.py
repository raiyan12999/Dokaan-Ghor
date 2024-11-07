from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("", views.index, name = "index"),
    path("form/", views.form, name = "form"),
    path("product/<int:pk>/", views.product, name = "product"),
    path("cart/<int:pk>/", views.cart, name = "cart"),
    path("sold/<int:pk>/", views.sold, name = "sold")
]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)