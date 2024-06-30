from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('create_vendor/', views.create_vendor, name='create_vendor'),
    path('vendor_admin/', views.vendor_admin, name='vendor_admin'),
    path('add_product/', views.add_product, name='add_product'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='vendor/login.html'), name='login'),
]