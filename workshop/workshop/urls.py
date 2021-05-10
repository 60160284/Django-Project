"""workshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path


from store import views
from django.conf.urls.static import static
from django.conf import settings
from django.utils.translation.trans_real import DjangoTranslation
urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('',views.index,name="home"),
    path('category/<slug:category_slug>',views.index,name="product_by_category"),
    path('typefile/<slug:typefile_slug>',views.index,name="product_by_typefile"),
    path('published/<slug:published_slug>',views.index,name="product_by_published"),

    path('product/<slug:category_slug>/<slug:product_slug>',views.productPage,name='productDetail'),
    
    
   
    path('upload/',views.uploadView, name="upLoad"),
    path('upload/workspace',views.workspace_list,name="workspace"),


    path('account/create',views.SignUpView, name="signUp"),
    path('account/login',views.SignInView, name="signIn"),
    path('account/reset',views.resetPass, name="resetPass"),
    path('account/logout',views.signOutView,name="signOut"),
    path('account/profile',views.profileView,name="proFile"),
    
    
    
]

if settings.DEBUG :

    #/mediaproduct
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    
    #/static/
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
