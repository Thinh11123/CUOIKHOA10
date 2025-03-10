from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Product,Order
from .forms import OrderForm


def home(request):
    product_list = Product.objects.all()
    paginator = Paginator(product_list, 6) #hiển thị 6 sản phẩm trên mỗi trang
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'index.html', {'page_obj': page_obj})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', {'product': product})
def place_order(request,pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.product = product
            order.save()
            return redirect('order_success')
    else:
        form = OrderForm()
    return render (request,'place_order.html',{'product':product,'form':form})
def order_success(request):
    return render(request,'order_success.html')



