from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
# Create your views here.

def register(request):
    form=UserCreationForm()
    if request.method=="POST":
        form= UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f"Welcome {username}, your account has been created")

            return redirect("myapp:index")


    return render(request,'users/register.html',{"form":form})