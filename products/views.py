from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from .models import Product

def index(request):
    # Logica
    products = Product.objects.all()
    return render(request,"list_of_products.html",{"products": products})