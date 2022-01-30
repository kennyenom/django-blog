from django.shortcuts import redirect, render
from .models import *
from .forms import OrderForm, ProductForm
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.

def index(request):
    order = Order.objects.all()
    products = Product.objects.all()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
           instance =  form.save(commit=False)
           instance.staff = request.user
           instance.save()
    else:
        form = OrderForm()
    context = {
        'order':order,
        'form':form,
        'products':products
    }
    return render(request,'dashboard/index.html',context)

def staff(request):
    workers = User.objects.all()
    workers_count = workers.count()
    context = {
        'workers':workers,
        'workers_count':workers_count
    }
    return render(request,'dashboard/customers.html',context)

def customer_detail(request,pk=None):
    customers = User.objects.get(id=pk)
    context ={
        'customers':customers
    }
    
    return render(request,'dashboard/customer_detail.html',context)
def product(request):
   # items = Product.objects.all()
    items = Product.objects.raw('SELECT * FROM dashboard_product')
    product_count = Product.objects.all().count()
    if request.method == 'POST':
        form = ProductForm(request.POST)

        if form.is_valid():
            form.save()
            product_name = form.cleaned_data.get('name')
            messages.success(request,f"{product_name} was added succesfully")
            return redirect('product')
    else:
        form = ProductForm()
    context = {
        'items':items,
        'form':form,
        'product_count':product_count
        
        

    }
    return render(request,'dashboard/products.html',context)
def order(request):
    order =  Order.objects.all()
    order_count = Order.objects.all().count()
    context = {
        'order':order,
        'order_count':order_count
    }
    return render(request,'dashboard/order.html',context)
def products_detail(request,pk=None):
    context = {
    }
    return render(request,'dashboard/products_detail.html',context)

def products_edit(request,pk=None):
    item = Product.objects.get(id=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST,instance=item)
        if form.is_valid():
            form.save()         
    else:
        form = ProductForm(instance=item)
    context = {
        'form':form
    }
    return render(request,'dashboard/products_edit.html',context)

def product_delete(request,pk=None):
    form = Product.objects.get(id=pk)
    if request.method == 'POST':
         form.delete()
         return redirect('product')
    return render(request,'dashboard/products_delete.html')

