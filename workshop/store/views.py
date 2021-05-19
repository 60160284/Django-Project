from django.shortcuts import render,get_object_or_404,redirect


from django.contrib.auth.models import Group, User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login , authenticate,logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator,EmptyPage,InvalidPage

from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Profile, UploadFile , Category,Typefile,Published
from .forms import UploadFileForm, ProfileUpdateForm, UserUpdateForm,  SignUpForm
from .mixins import UploadOwnerMixin

from django.db.models.signals import post_save

def paymentView(request):
    return render(request, 'payment.html')




@login_required
def uploadView(request):
    
        if request.method == 'POST':
            form = UploadFileForm(request.POST, request.FILES)
            
            if form.is_valid():
               
                form.save(commit=False)
                form.user =request.user
                form.save()
                return redirect('workspace')

        else:
            form = UploadFileForm()
            
        return render(request, 'uploads/upload_form.html', {'form':form})

    



def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)
    


def workspaceView(request):
    uploads=UploadFile.objects.all().filter(user=request.user)
    return render(request,'workspace.html',{'uploads':uploads})
    

def index(request, category_slug=None):
    uploads = None
    category_page=None
    
    if category_slug!=None:
        category_page=get_object_or_404(Category,slug=category_slug)
        uploads=UploadFile.objects.all().filter(category=category_page)
    else :
        uploads=UploadFile.objects.all().filter()

    
    paginator=Paginator(uploads,8)
    try:
        page=int(request.GET.get('page','1'))
    except:
        page=1

    try:
        uploadperPage=paginator.page(page)
    except (EmptyPage,InvalidPage):
        uploadperPage=paginator.page(paginator.num_pages)

    return render(request,'index.html',{'uploads':uploadperPage,'category':category_page})








def indextype(request, typefile_slug=None):
    uploads = None
    typefile_page=None
    
    if typefile_slug!=None:
        typefile_page=get_object_or_404(Typefile,slug=typefile_slug)
        uploads=UploadFile.objects.all().filter(typefile=typefile_page)
    else :
        uploads=UploadFile.objects.all().filter()


    return render(request,'index.html',{'uploads':uploads,'typefile':typefile_page})



def indexpub(request, published_slug=None):
    uploads = None
    published_page=None
    
    if published_slug!=None:
        published_page=get_object_or_404(Published,slug=published_slug)
        uploads=UploadFile.objects.all().filter(published=published_page)
    else :
        uploads=UploadFile.objects.all().filter()


    return render(request,'index.html',{'uploads':uploads,'published':published_page})






def uploadProductPage(request, category_slug, uploadfile_slug):
    try:
        uploads=UploadFile.objects.get(category__slug=category_slug,slug=uploadfile_slug)
    except Exception as e :
        raise e
    return render(request,'uploads/upload_detail.html',{'uploads':uploads})



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
        else:
            print(form.errors)
            
            messages.error(request,'ขออภัย, มีบางอย่าผิดพลาด โปรดกรอกข้อมูลอีกครั้ง')
            return redirect('signUp')
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
    uploads=UploadFile.objects.filter(name__contains=request.GET['title'])
    
    return render(request,'index.html',{'uploads':uploads})

@login_required
def profileView(request):
  
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('proFile')

    else:
       
        u_form = UserUpdateForm(instance=request.user)
        
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }


    return render(request, 'profile.html', context)




class PostListView(ListView):
	model = UploadFile





class PostCreateView(LoginRequiredMixin, CreateView):
	model = UploadFile
	form_class = UploadFileForm

	def form_valid(self, form, *args, **kwargs):
		# print(form)
		# print(self)
		# print(args)
		# print(kwargs)
		upload = form.save(commit=False)

		# print(self.request.user)
		# print(post.title, post.message)

		upload.user = self.request.user
		upload.save()
		return super().form_valid(form)

class PostUpdateView(UploadOwnerMixin, UpdateView):
	model = UploadFile
	form_class = UploadFileForm

class PostDeleteView(UploadOwnerMixin, DeleteView):
	model = UploadFile
	success_url = reverse_lazy('')