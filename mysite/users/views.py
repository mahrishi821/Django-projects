from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import RegisterForms
from django.contrib.auth import logout
# Create your views here.

def register(request):
    form=RegisterForms()
    if request.method=="POST":
        form= RegisterForms(request.POST)

        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f"Welcome {username}, your account has been created")

            return redirect("login")


    return render(request,'users/register.html',{"form":form})

def logout_view(request):
    logout(request)
    return render(request,'users/logout.html')