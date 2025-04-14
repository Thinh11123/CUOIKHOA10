from django.db import models
from django.urls import reverse

class Product(models.Model):
    CATEGORY=[
        ('nike','nike'),
        ('adidas','adidas'),
    ]
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='products/')
    category = models.CharField(max_length=50,choices=CATEGORY,default='nike')
    def __str__(self):
        return self.name
    
    #Reverse là một hàm của django dùng để tạo URL từ
    # tên của URL pattern 
    def get_absolute_url(self):
        return reverse('product_detail', args=[str(self.id)])
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.TextField()
    phone = models.CharField(max_length=15)
    quantity = models.IntegerField()
    
    def __str__(self):
        return f"Order for {self.product.name} by {self.name}"