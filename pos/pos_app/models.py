from django.db import models

class Product(models.Model):
    product_name = models.CharField(max_length=255)
    price = models.FloatField()
    stock_quantity = models.IntegerField()
    barcode = models.CharField(max_length=255, unique=True)
    category = models.CharField(max_length=255)

class Customer(models.Model):
    customer_name = models.CharField(max_length=255)
    email = models.EmailField(null=True, blank=True)
    phone_number = models.CharField(max_length=255, null=True, blank=True)
    address = models.TextField()

class Sale(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='sales')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='sales')
    sale_date = models.DateTimeField(auto_now_add=True)
    total_amount = models.FloatField()
    payment_method = models.CharField(max_length=255)
    notes = models.TextField()
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='sales')

class SaleItem(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='sales')
    quantity = models.IntegerField()
    unit_price = models.FloatField()
    item_amount = models.FloatField()

class User(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='users')
    username = models.CharField(max_length=255, unique=True)
    password_hash = models.CharField(max_length=255)
    role = models.CharField(max_length=255, default='user')
    is_active = models.BooleanField(default=True)