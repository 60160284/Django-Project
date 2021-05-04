from django.contrib import admin
from store.models import Category, Product,Typefile,Published
# Register your models here.
admin.site.register(Category)
admin.site.register(Typefile)
admin.site.register(Published)
admin.site.register(Product)


admin.site.register(Profile)