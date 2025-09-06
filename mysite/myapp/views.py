from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from .models import Item
# Create your views here.

def index(request):
    items=Item.objects.all() # for queryset
    context={
        "item_list":items
    }
    # return HttpResponse(request,"myapp/index.html")
    return render(request,"myapp/index.html",context)

def detailview(request,id):
    item=Item.objects.get(id=id) # for an single item we can use this
    context={
        "item":item
    }
    return render(request,"myapp/detail.html",context)
    # return HttpResponse(f"Detail view for {item}")

def ReviewAPI(request):
    return HttpResponse("Review Called")
class testview(APIView):

    def post(self,request):
        return HttpResponse("request data")