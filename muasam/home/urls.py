from django.urls import path
from .views import home, product_detail,place_order,order_success

urlpatterns = [
    path('', home, name='home'),
    path('product/<int:pk>/', product_detail, name='product_detail'),
    path('product/<int:pk>/order/',place_order, name='place_order'),
    path('order_success/', order_success, name='order_success'),
]