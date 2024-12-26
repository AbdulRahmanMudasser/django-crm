from django import forms
from .models import *

# Order Form
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
       
# Customer Form 
class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        
        widgets = {
            field: forms.TextInput(attrs={'class': 'form-control'}) for field in fields
        }
   
# Product Form
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
         