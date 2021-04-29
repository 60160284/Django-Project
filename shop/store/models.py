from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=255,unique=True)
    slug=models.SlugField(max_length=255,unique=True)
      
    def __str__(self):
        return self.name

class Product(models.Model):
    name=models.CharField(max_length=255,unique=True)
    slug=models.SlugField(max_length=255,unique=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    #typefile=models.ForeignKey(Typefile,on_delete=models.CASCADE)
    #publishied=models.ForeignKey(Published,on_delete=models.CASCADE)
    
    inputfile=models.FileField(upload_to='inputfile/')
    image=models.ImageField(upload_to="product",blank=True)
    #available=models.BooleanField(default=True)
    
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
         
    def __str__(self):
        return self.name