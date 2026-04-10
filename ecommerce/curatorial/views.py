from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request, "homepage.html")

def shopping_cart(request):
    return render(request, "shopping_cart.html")
