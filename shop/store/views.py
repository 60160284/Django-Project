from django.shortcuts import render,get_object_or_404,redirect
from store.models import Category, Product,Typefile,Published
#from django.http import HttpResponse
# Create your views here.
from django.http import FileResponse
from store.forms import SignUpForm 
from django.contrib.auth.models import Group, User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login , authenticate,logout
from users import views as user_views

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





def uploadView(request):
    return render(request,'upload.html')


def resetPass(request):
    return render(request,'password_reset.html')

def SignUpView(request):
    if request.method=='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            #บันทึกข้อมูล User
            form.save()
            #บันทึก Group Customer
            #ดึง username จากแบบฟอร์มมาใช้
            username=form.cleaned_data.get('username')
            #ดึงข้อมูล user จากฐานข้อมูล
            signUpUser=User.objects.get(username=username)
            #จัด Group
            customer_group=Group.objects.get(name="Customer")
            customer_group.user_set.add(signUpUser)
        
           
    else :
        form=SignUpForm()
    return render(request,"signup.html",{'form':form})


def SignInView(request):
    if request.method=='POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            username=request.POST['username']
            password=request.POST['password']
            user=authenticate(username=username,password=password)
            if user is not None :
                login(request,user)
                return redirect('home')
            else :
                return redirect('signUp')
    else:
        form=AuthenticationForm()
    return render(request,'signIn.html',{'form':form})

     

def signOutView(request):
    logout(request)
    return redirect('signIn')


   


def profileView(request):
    if request.method == 'POST':
       
      
       
    return render(request, 'profile.html', args)