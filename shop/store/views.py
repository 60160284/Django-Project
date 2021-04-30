from django.shortcuts import render
from store.models import Category, Product,Typefile,Published
#from django.http import HttpResponse
# Create your views here.

def index(request):
    products = None
    products=Product.objects.all().filter()
    return render(request,'index.html',{'products' :products})

def product(request):
   return render(request,'product.html')