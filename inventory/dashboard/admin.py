from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import *
# Register your models here.

admin.site.site_header = 'Enom'
class ProductAdmin(admin.ModelAdmin):
    list_diplay=('name','category','quantity',)
admin.site.register(Product,ProductAdmin)

class OrderAdmin(admin.ModelAdmin):
    list_display =  ('product','quantity','date')
admin.site.register(Order,OrderAdmin)
