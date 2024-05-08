from django.contrib import admin
from . models import UserProfile, Income, Product, Category

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Income)
admin.site.register(Category)
admin.site.register(Product)



