from django.urls import path
from .views import product, product_detail,place_order,order_success,home,nike_pd,adidas_pd,contact

urlpatterns = [
    path('product/', product, name='product'),
    path('product/<int:pk>/', product_detail, name='product_detail'),
    path('product/<int:pk>/order/',place_order, name='place_order'),
    path('order_success/', order_success, name='order_success'),
    path('',home, name='home'),
    path('nike/',nike_pd,name='nike'),
    path('adidas_pd',adidas_pd,name='adidas'),
    path('contact/',contact,name='contact')
]