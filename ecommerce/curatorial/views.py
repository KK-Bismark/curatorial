from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request, "homepage.html")

def shopping_cart(request):
    return render(request, "shopping_cart.html")

def product_details(request):
    return render(request, "product_details.html")

def product_catalog(request):
    return render(request, "product_catalog.html")