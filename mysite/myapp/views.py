from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from .models import Item
# Create your views here.

def index(request):
    items=Item.objects.all()
    return HttpResponse(items)

def ReviewAPI(request):
    return HttpResponse("Review Called")
class testview(APIView):

    def post(self,request):
        return HttpResponse("request data")