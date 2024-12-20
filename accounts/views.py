from django.shortcuts import render
from .models import *

# Home View
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

# Products View
def products(request):
    # Get Products
    products = Product.objects.all()
    
    context = {
        'products': products
    }
    
    return render(request, 'accounts/product.html', context)

# Customer View
def customer(request, pk):
    # Get Customer With id
    customer = Customer.objects.get(id=pk)
    
    # Get Orders Placed By Customer
    orders = customer.order_set.all()
    
    # Get Orders Count Placed By Customer
    orders_count = orders.count()
    
    context = {
        'customer': customer,
        'orders': orders,
        'orders_count': orders_count,
    }
    
    return render(request, 'accounts/customer.html', context)

# Create Order View
def create_order(request):
    context = {}
    
    return render(request, 'accounts/order_form.html', context)
