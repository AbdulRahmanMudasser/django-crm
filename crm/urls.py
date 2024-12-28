from django.contrib import admin
from django.urls import path

from accounts import views

urlpatterns = [
    # Admin Panel URL
    path('admin/', admin.site.urls),  
    
    # Login URL
    path('login/', views.login, name='login'),
    
    # Register URL
    path('register/', views.register, name='register'),
    
    # Home Page URL
    path('', views.home, name='home'),
    
    # View Products URL
    path('products/', views.products, name='products'),
    
    # Create Product URL
    path('create_product/', views.create_product, name='create_product'),
    
    # Update Product URL
    path('update_product/<str:pk>', views.update_product, name='update_product'),
    
    # Delete Product URL
    path('delete_product/<str:pk>', views.delete_product, name='delete_product'),
    
    # View Customers URL
    path('customers/<str:pk>', views.customer, name='customer'),
    
    # Create Order URL
    path('create_order/<str:pk>', views.create_order, name='create_order'),
    
    # Update Order URL
    path('update_order/<str:pk>', views.update_order, name='update_order'),
    
    # Delete Order URL
    path('delete_order/<str:pk>', views.delete_order, name='delete_order'),
    
    # Create Customer URL
    path('create_customer/', views.create_customer, name='create_customer'),
    
    # Update Customer URL
    path('update_customer/<str:pk>', views.update_customer, name='update_customer'),
    
    # Delete Customer URL
    path('delete_customer/<str:pk>', views.delete_customer, name='delete_customer'),
]
