from django_filters import FilterSet, DateFilter
from .models import *

# Order Filter
class OrderFilter(FilterSet):
    start_date = DateFilter(field_name='date_created', lookup_expr='gte', label='Orders Placed After')
    end_date = DateFilter(field_name='date_created', lookup_expr='lte', label='Orders Placed Before')
    
    class Meta:
        model = Order
        fields = '__all__'
        exclude = ['customer', 'date_created']
        