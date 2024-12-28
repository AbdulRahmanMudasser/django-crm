from django.shortcuts import render, redirect, get_object_or_404
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from .models import *
from .filters import *

# Login View
def login(request):
    context = {}
    
    # Render Login Template
    return render(request, 'accounts/login.html', context)

# Register User View
def register(request):
    # Create Form
    form = UserCreationForm()
    
    # Check if Request Method is POST
    if request.method == 'POST':
        # Process Submitted Data
        form = UserCreationForm(request.POST)
        
        # Check if Form is Valid
        if form.is_valid():
            # Save Form
            form.save()
            
            return redirect('home')
    
    context = {
        'form': form,
    }
    
    # Render Register Template
    return render(request, 'accounts/register.html', context)

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
    
    # Get Orders Out for Delivery
    out_for_delivery_orders = orders.filter(status="Out for Delivery").count()
    
    context = {
        'customers': customers,
        'orders': orders,
        'total_customers': total_customers,
        'total_orders': total_orders,
        'delivered_orders': delivered_orders,
        'pending_orders': pending_orders,
        'out_for_delivery_orders': out_for_delivery_orders,
    }
    
    # Render Dashboard Template
    return render(request,'accounts/dashboard.html', context)

# Products View
def products(request):
    # Get Products
    products = Product.objects.all()
    
    # Get Products Count
    products_count = Product.objects.all().count()
    
    context = {
        'products': products,
        'products_count': products_count,
    }
    
    # Render Products Template
    return render(request, 'accounts/product.html', context)

# Create Product View
def create_product(request):
    # Product Form
    form = ProductForm()
    
    # Check Request Method is POST
    if request.method == 'POST':
        form = ProductForm(request.POST)
        
        # Check if Form is Valid
        if form.is_valid():
            # Save Form
            form.save()
            
            # Redirect to Product List Template
            return redirect('products')
            
    context = {
        'form': form,
        'function': 'Create New Product'
    }
    
    # Render Product Form Template
    return render(request, 'accounts/product_form.html', context)

# Update Product View
def update_product(request, pk):
    # Get Product With id
    product = get_object_or_404(Product, id=pk)
    
    # Product Form
    form = ProductForm(instance=product)
    
    # Check if Request Method is POST
    if request.method == 'POST':
        # Process Submitted Data
        form = ProductForm(request.POST, instance=product)
        
        # Check if Form is Valid
        if form.is_valid():
            # Save Form
            form.save()
            
            # Redirect to Products Template
            return redirect('products')
        
    context = {
        'form': form,
        'function': 'Update Product'
    }
    
    # Render Product Form Template
    return render(request, 'accounts/product_form.html', context)

# Delete Product View
def delete_product(request, pk):
    # Get Product With id
    product = get_object_or_404(Product, id=pk)
    
    # Check if Request Method is POST
    if request.method == 'POST':
        # Delete Product
        product.delete()
        
        # Redirect to Products Template
        return redirect('products')
    
    context = {
        'product': product,
    }
    
    # Render Delete Product Template
    return render(request, 'accounts/delete_product.html', context)

# Customer View
def customer(request, pk):
    # Get Customer With id
    customer = Customer.objects.get(id=pk)
    
    # Get Orders Placed By Customer
    orders = customer.order_set.all()
    
    # Get Orders Count Placed By Customer
    orders_count = orders.count()
    
    # Order Filter
    filter = OrderFilter(request.GET, queryset=orders)
    
    # Searched Orders
    orders = filter.qs
    
    context = {
        'customer': customer,
        'orders': orders,
        'orders_count': orders_count,
        'filter': filter,
    }
    
    # Render Customers Template
    return render(request, 'accounts/customer.html', context)

# Create Order View
def create_order(request, pk):
    # Instance of Form Set
    OrderFormSet = inlineformset_factory(Customer, Order, fields=('product', 'status'), can_delete=False, extra=3)
    
    # Get Customer With pk
    customer = get_object_or_404(Customer, id=pk)
    
    # Order Form
    # form = OrderForm(initial={'customer': customer})
    
    # Order Form Set
    form = OrderFormSet(queryset=Order.objects.none(), instance=customer)
    
    if request.method == 'POST':
        # Process Submitted Data
        # form = OrderForm(request.POST)
        
        # Process Submitted Data
        form = OrderFormSet(request.POST, instance=customer)
        
        # Check if Form is Valid
        if form.is_valid():
            # Save Form
            form.save()
            
            # Redirect to Home Page
            return redirect('home')
    
    context = {
        'form': form,
        'function': 'Create Order'
    }
    
    # Render Order Form Template
    return render(request, 'accounts/order_form.html', context)

# Update Order View
def update_order(request, pk):
    # Get Order With id
    order = Order.objects.get(id=pk)
    
    # Order Form
    form = OrderForm(instance=order)
    
    if request.method == 'POST':
        # Process Submitted Data
        form = OrderForm(request.POST, instance=order)
        
        # Check if Form is Valid
        if form.is_valid():
            # Save Form
            form.save()
            
            # Redirect to Home Page
            return redirect('home')
    
    context = {
        'form': form,
        'function': 'Update Order'
    }
    
    # Render Order Form Template
    return render(request, 'accounts/order_form.html', context)

# Delete Order View
def delete_order(request, pk):
    # Get Order With id
    order = Order.objects.get(id=pk)
    
    if request.method == 'POST':
        # Delete Order
        order.delete()
        
        # Redirect to Home Page
        return redirect('home')
    
    context = {
        'order': order,
    }
    
    # Render Delete Order Template
    return render(request, 'accounts/delete_order.html', context)

# Create Customer View
def create_customer(request):
    # Customer Form
    form = CustomerForm()
    
    if request.method == 'POST':
        # Process Submitted Data
        form = CustomerForm(request.POST)
        
        # Check if Form is Valid
        if form.is_valid():
            # Save Form
            form.save()
            
            # Redirect to Home Page
            return redirect('home')
    
    context = {
        'form': form,
        'function': 'Create Customer'
    }
    
    # Render Customer Form Template
    return render(request, 'accounts/customer_form.html', context)

# Update Customer View
def update_customer(request, pk):
    # Get Customer With id
    customer = get_object_or_404(Customer, id=pk)
    
    # Customer Form
    form = CustomerForm(instance=customer)
    
    # Check if Request Method is POST
    if request.method == 'POST':
        # Process Submitted Data
        form = CustomerForm(request.POST, instance=customer)
        
        # Check if Form is Valid
        if form.is_valid():
            # Save Form
            form.save()
            
            # Redirect to Current Customer Form With id
            return redirect(f'/customers/{pk}')
        
    context = {
        'form':form,
        'function': 'Update Customer',
    }
    
    # Render Customer Form Template
    return render(request, 'accounts/customer_form.html', context)

# Delete Customer View
def delete_customer(request, pk):
    # Get Customer With id
    customer = get_object_or_404(Customer, id=pk)
    
    # Check if Request Method is POST
    if request.method == 'POST':
        # Delete Customer
        customer.delete()
        
        # Redirect to Home Page
        return redirect('home')
    
    context = {
        'customer': customer,
    }
    
    # Render Delete Customer Template
    return render(request, 'accounts/delete_customer.html', context)
        