from django.shortcuts import render, viewsets
from rest_framework import viewsets
from .models import Product, Customer, Sale, SaleItem, User
from .serializer import ProductSerializer, CustomerSerializer, SaleSerializer, SaleItemSerializer, UserSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class SaleViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer

class SaleItemViewSet(viewsets.ModelViewSet):
    queryset = SaleItem.objects.all()
    serializer_class = SaleItemSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

def frontend(request):
    context ={
      'title':'some frontend title'
    }
    return render(request, 'frontend.html', context)