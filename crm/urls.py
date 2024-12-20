from django.contrib import admin
from django.urls import path

from accounts import views

urlpatterns = [
    path('admin/', admin.site.urls),    
    path('', views.home, name='home'),
    path('products/', views.products, name='products'),
    path('customers/<str:pk>', views.customer, name='customer'),
    path('create_order', views.create_order, name='create_order'),
]
