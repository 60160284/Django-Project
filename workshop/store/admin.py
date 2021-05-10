
from django.contrib import admin
from store.models import Category, Product,Typefile,Published,UploadFile,Profile
# Register your models here.




class ProductAdmin(admin.ModelAdmin):
    list_display=['name','price','created','updated']
    list_editable=['price']
      


admin.site.register(Category)
admin.site.register(Typefile)
admin.site.register(Published)
admin.site.register(Product, ProductAdmin)



admin.site.register(UploadFile)
admin.site.register(Profile)
# Register your models here.
