from django.shortcuts import render
from . cart import Cart

# Create your views here.
def cart_detail(request):
    cart = Cart(request)

    return render(request, 'cart/cart.html')

