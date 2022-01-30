from django import forms
from django.db.models import fields

from .models import *


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name','category','quantity']

# class Productedit(forms.ModelForm):
#     class Meta:
#         model = Product
#         fields = ['name','category','quantity']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['product','quantity']