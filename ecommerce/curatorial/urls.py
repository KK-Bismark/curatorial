from django.urls import path
from .views import homepage, shopping_cart, product_details


urlpatterns = [
        path("", homepage, name="homepage"),
        path("cart/", shopping_cart, name="shopping_cart"),
        path("product_details/", product_details, name="product_details")
        ]
