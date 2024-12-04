from django.shortcuts import render

def home(request):
    return render(request=request, template_name='accounts/dashboard.html')

def products(request):
    return render(request=request, template_name='accounts/product.html')

def customer(request):
    return render(request=request, template_name='accounts/customer.html')
