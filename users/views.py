from importlib.resources import contents
from multiprocessing import context
import profile
from telnetlib import AUTHENTICATION
from urllib import request
from wsgiref.util import request_uri
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from .forms import UserForm , UserProfileForm

# Create your views here.

#  def register(request):

#    if  request.method =="POST":
#        form =UserCreationForm(request.POST) #hazır formu kullandık 
#        if form.is_valid():
#            form.save()
#            username = form.cleaned_data['username']
#            password = form.cleaned_data['password1']

#            user =authenticate(username=username,password=password) #save de kaydedilen datadan authenticate için gerekli bilg. aldık.
#            login(request,user)
#            return redirect('home')
#    else:
#        form = UserCreationForm()

#    return render(request, 'registration/register.html',{'form':form})

def register(request):
    form_user =UserForm()
    form_profile =UserProfileForm()
    if request.method =="POST":
        form_user =UserForm(request.POST)
        form_profile =UserProfileForm(request.POST, request.FILES)
        if form_user.is_valid() and form_profile.is_valid():
            user =form_user()
            profile =form_profile().save(commit=False) # bilgilerin kime ait olduığu user almadığı için böyle yaptık 
            profile.user=user # sanki dic. ekler gibi 'user=user'
            profile.save()
            
            login(request,user)

            return redirect('home')
    context = {
        'form_user': form_user,
        'form_profile': form_profile
    }
    return render(request,'users/register.html',context) 

