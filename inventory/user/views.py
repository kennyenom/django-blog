from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
from .forms import *
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = Creationform(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f"{username} created succesfully login here to continue")
            return redirect('login')
    else:
        form = Creationform()
    context = {
        'form':form
    }
    return render(request,'user/register.html',context)

def profile(request):
    context = {}
    return render(request,'user/profile.html',context)

def profile_update(request):
    if request.method== 'POST':
        user_form = UserUpdateForm(request.POST,instance=request.user)
        profile_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
   
    context = {
        'user_form':user_form,
        'profile_form':profile_form
    }
    return render(request,'user/profile_update.html',context)