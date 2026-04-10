from django.urls import path
from .views import homepage, product_catalog, product_details, shopping_cart


urlpatterns = [
        path("", homepage, name="homepage"),
        path("product_catalog/", product_catalog, name="product_catalog"),
        path("product_details/", product_details, name="product_details"),
        path("cart/", shopping_cart, name="shopping_cart"),
        ]
