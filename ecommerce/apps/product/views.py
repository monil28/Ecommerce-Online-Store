import random
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from . models import Product, Category
from . forms import AddToCartForm
from apps.cart.cart import Cart
from django.contrib import messages

# Create your views here.

def search(request):
    query = request.GET.get('query', '')
    products = Product.objects.filter(Q(title__contains=query) | Q(description__contains=query))

    return render(request, 'product/search.html', {'products': products, 'query': query})

def category(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    
    return render(request, 'product/category.html', {'category': category})

def product(request, category_slug, product_slug):
    product = get_object_or_404(Product, category__slug=category_slug, slug=product_slug)
    cart = Cart(request)
    if request.method == "POST":
        form = AddToCartForm(request.POST)
        if form.is_valid():
            quantity = form.cleaned_data('quantity')
            cart.add(product_id=product.id, quantity=quantity, update_quantity=False)
            messages.success(request, "Product is added to the cart")
            return redirect('product', category_slug=category_slug, product_slug=product_slug)
    else:
        form = AddToCartForm()
            

    similar_products = list(product.category.products.exclude(id=product.id))

    if len(similar_products)>=4:
        similar_products = random.sample(similar_products, 4)

    return render(request, 'product/product.html', {'form': form, 'product': product, 'similar_products': similar_products})