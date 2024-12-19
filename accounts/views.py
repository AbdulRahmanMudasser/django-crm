from django.shortcuts import render
from .models import *

def home(request):
    # Get Customers
    customers = Customer.objects.all()
    
    # Get Orders
    orders = Order.objects.all()
    
    # Get Customers Count
    total_customers = customers.count()
    
    # Get Orders Count
    total_orders = orders.count()
    
    # Get Delivered Orders Count
    delivered_orders = orders.filter(status="Delivered").count()
    
    # Get Pending Orders Count
    pending_orders = orders.filter(status="Pending").count()
    
    context = {
        'customers': customers,
        'orders': orders,
        'total_customers': total_customers,
        'total_orders': total_orders,
        'delivered_orders': delivered_orders,
        'pending_orders': pending_orders,
    }
    
    return render(request,'accounts/dashboard.html', context)

def products(request):
    # Get Products
    products = Product.objects.all()
    
    context = {
        'products': products
    }
    
    return render(request, 'accounts/product.html', context)

def customer(request):
    return render(request=request, template_name='accounts/customer.html')
