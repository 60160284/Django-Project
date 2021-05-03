from django.shortcuts import render,get_object_or_404
from store.models import Category, Product,Typefile,Published
#from django.http import HttpResponse
# Create your views here.
from django.http import FileResponse
from store.forms import SignUpForm 

def index(request, category_slug=None):
    products = None
    category_page=None
    if category_slug!=None:
        category_page=get_object_or_404(Category,slug=category_slug)
        products=Product.objects.all().filter(category=category_page)
    else :
        products=Product.objects.all().filter()

    
    return render(request,'index.html',{'products':products,'category':category_page})


#def product(request):
   #return render(request,'product.html')
def productPage(request, category_slug, product_slug):
    try:
        product=Product.objects.get(category__slug=category_slug,slug=product_slug)
    except Exception as e :
        raise e
    return render(request,'product.html',{'product':product})



def signinView(request):
    return render(request,'signin.html')


def uploadView(request):
    return render(request,'upload.html')



def SignUpView(request):
    form=SignUpForm()
    return render(request,'signup.html',{'form':form})


