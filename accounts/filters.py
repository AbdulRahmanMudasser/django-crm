from django_filters import FilterSet, DateFilter, CharFilter
from django.forms import TextInput, DateInput
from .models import Order

# Order Filter
class OrderFilter(FilterSet):
    start_date = DateFilter(
        field_name='date_created', 
        lookup_expr='gte', 
        label='Orders Placed After',
        widget=DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )
    end_date = DateFilter(
        field_name='date_created', 
        lookup_expr='lte', 
        label='Orders Placed Before',
        widget=DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )
    product = CharFilter(
        field_name='product__name',
        lookup_expr='icontains',
        label='Product',
        widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'Search Product'})
    )
    status = CharFilter(
        field_name='status',
        lookup_expr='icontains',
        label='Status',
        widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Status'})
    )

    class Meta:
        model = Order
        fields = '__all__'
        exclude = ['customer', 'date_created']
