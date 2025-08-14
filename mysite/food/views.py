from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Hello world")

def item(request):
    return HttpResponse("This is an item view")

def foot(request):
    return HttpResponse("<h1>This is an foot view</h1>") #can also pass the the html