from django.urls import path
from .views import homepage, shopping_cart


urlpatterns = [
        path("", homepage, name="homepage"),
        path("cart/", shopping_cart, name="shopping_cart"),
        ]
