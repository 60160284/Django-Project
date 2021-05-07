from django.db import models
from django.urls import reverse
from django.http import FileResponse
from django.contrib.auth.forms import User


# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=255,unique=True)
    slug=models.SlugField(max_length=255,unique=True)

    def __str__(self):
        return self.name

    
    class Meta :
        ordering=('name',)
        verbose_name ='หมวดหมู่'
        verbose_name_plural = "ข้อมูลหมวดหมู่"

    def get_url(self):
        return reverse('product_by_category',args=[self.slug])

class Typefile(models.Model):
    name=models.CharField(max_length=255,unique=True)
    slug=models.SlugField(max_length=255,unique=True)
      
    def __str__(self):
        return self.name

    class Meta :
        ordering=('name',)
        verbose_name ='รูปแบบ'
        verbose_name_plural = "ข้อมูลรูปแบบ"


    def get_url(self):
        return reverse('product_by_typefile',args=[self.slug])

class Published(models.Model):
    name=models.CharField(max_length=255,unique=True)
    slug=models.SlugField(max_length=255,unique=True)
      
    def __str__(self):
        return self.name

    class Meta :
        ordering=('name',)
        verbose_name ='การเผยแพร่'
        verbose_name_plural = "ข้อมูลการเผยแพร่"

    def get_url(self):
        return reverse('product_by_published',args=[self.slug])

class Product(models.Model):
    name=models.CharField(max_length=255,unique=True)
    slug=models.SlugField(max_length=255,unique=True)
    description=models.TextField(blank=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    typefile=models.ForeignKey(Typefile,on_delete=models.CASCADE)
    published=models.ForeignKey(Published,on_delete=models.CASCADE)
    
    inputfile=models.FileField(upload_to='inputfile/')
    image=models.ImageField(upload_to="product",blank=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    #available=models.BooleanField(default=True)
    
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
         
    def __str__(self):
        return self.name

    class Meta :
        ordering=('name',)
        verbose_name='สินค้า'
        verbose_name_plural="ข้อมูลสินค้า"


    def get_url(self):
        return reverse('productDetail',args=[self.category.slug,self.slug])



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_pics')
    
    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

 

class Upload(models.Model):
    name=models.CharField(max_length=255,unique=True)
    description=models.TextField(blank=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    typefile=models.ForeignKey(Typefile,on_delete=models.CASCADE)
    published=models.ForeignKey(Published,on_delete=models.CASCADE)
    
    inputfile=models.FileField(upload_to='user/inputfile/')
    image=models.ImageField(upload_to='user/product/', null=True, blank=True)

    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
       
        self.inputfile.delete()
        self.image.delete()
        super().delete(*args, **kwargs)