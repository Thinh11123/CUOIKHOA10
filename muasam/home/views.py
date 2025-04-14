from django.shortcuts import render, get_object_or_404,redirect
from django.core.paginator import Paginator
from .models import Product,Order
from .forms import OrderForm


def product(request):
    product_list = Product.objects.all()
    paginator = Paginator(product_list, 6) #hiển thị 6 sản phẩm trên mỗi trang
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'index.html', {'page_obj': page_obj})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', {'product': product})
def place_order(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.product = product
            order.save()
            return redirect('order_success')  # ← Sửa chỗ này: tên view, không phải tên file .html
    else:
        form = OrderForm()
    return render(request, 'place_order.html', {'product': product, 'form': form})
def order_success(request):
    return render(request,'order_success.html')
def home(request):
    return render(request,'home.html')
def nike_pd(request):
    product=Product.objects.filter(category='nike')
    return render(request, 'nike.html',{'products':product})
def adidas_pd(request):
    product=Product.objects.filter(category='adidas')
    return render(request, 'adidas.html',{'products':product})
def contact(request):
    return render(request,'contact.html')

