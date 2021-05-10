from django.shortcuts import render,get_object_or_404,redirect

from django.http import HttpResponseRedirect
# Create your views here.
from django.http import FileResponse
from django.contrib.auth.models import Group, User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login , authenticate,logout

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator,EmptyPage,InvalidPage
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy


from .models import Product, Profile
from .forms import UploadFileForm, ProfileUpdateForm, UserUpdateForm
from store.forms import SignUpForm
from store.models import Category, Product,Typefile,Published
from django.db.models.signals import post_save

def uploadView(request):
    
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save().format(instance.user.id, filename)
            return redirect('workspace')

    else:
        form = UploadFileForm()

    return render(request, 'upload.html', {'form':form})
    

    


def workspace_list(request):
    #uploads = Upload.objects.all()
    return render(request, 'workspace.html')




def index(request, category_slug=None):
    products = None
    category_page=None
    
    if category_slug!=None:
        category_page=get_object_or_404(Category,slug=category_slug)
        products=Product.objects.all().filter(category=category_page)
    else :
        products=Product.objects.all().filter()

    
    paginator=Paginator(products,8)
    try:
        page=int(request.GET.get('page','1'))
    except:
        page=1

    try:
        productperPage=paginator.page(page)
    except (EmptyPage,InvalidPage):
        productperPage=paginator.page(paginator.num_pages)

    return render(request,'index.html',{'products':productperPage,'category':category_page})


#def product(request):
   #return render(request,'product.html')
def productPage(request, category_slug, product_slug):
    try:
        product=Product.objects.get(category__slug=category_slug,slug=product_slug)
    except Exception as e :
        raise e
    return render(request,'product.html',{'product':product})






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
        return redirect('signIn')
           
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


def search(request):
    products=Product.objects.filter(name__contains=request.GET['title'])
    
    return render(request,'index.html',{'products':products})

@login_required
def profileView(request):
    
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        #p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile_image)
        if u_form.is_valid() :#and p_form.is_valid():
            u_form.save()
            #p_form.save()
            return redirect('proFile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        #p_form = ProfileUpdateForm(instance=request.user.profile_image)

    context = {
        'u_form': u_form,
        #'p_form': p_form
    }


    return render(request, 'profile.html', context)
