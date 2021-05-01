from django.shortcuts import render,get_object_or_404
from store.models import Category, Product,Typefile,Published
#from django.http import HttpResponse
# Create your views here.

def index(request, category_slug=None):
    products = None
    category_page=None
    if category_slug!=None:
        category_page=get_object_or_404(Category,slug=category_slug)
        products=Product.objects.all().filter(category=category_page)
    else :
        products=Product.objects.all().filter()

    
    return render(request,'index.html',{'products':products,'category':category_page})

def product(request):
   return render(request,'product.html')


def signupView(request):
    return render(request,'signup.html')

def signinView(request):
    return render(request,'signin.html')