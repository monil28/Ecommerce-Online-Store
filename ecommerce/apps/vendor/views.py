from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.utils.text import slugify
from . models import Vendor
# from apps.product.models import Product
from . forms import ProductForm

# Create your views here.
def create_vendor(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            vendor = Vendor.objects.create(name=user.username, created_by=user)
            return redirect('frontpage')
    else:
        form = UserCreationForm()

    return render(request, 'vendor/create_vendor.html', {'form': form})

@login_required
def vendor_admin(request):
    # print(dir(request))
    # print("User", request.user)
    # print(dir(request.user.monil.products.all()))
    vendor = request.user.vendor_user
    products = vendor.products.all()
    return render(request, 'vendor/vendor_admin.html', {'vendor': vendor, 'products': products})

@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():
            product = form.save(commit=False)
            product.vendor = request.user.vendor_user
            product.title = slugify(product.title)
            form.save()

            return redirect('vendor_admin')
    else:
        form=ProductForm()

    return render(request, 'vendor/add_product.html', {'form': form})
