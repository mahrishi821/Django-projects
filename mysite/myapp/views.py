from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
# Create your views here.

def index(request):
    return HttpResponse("hehehhehe")

def ReviewAPI(request):
    return HttpResponse("Review Called")
class testview(APIView):

    def post(self,request):
        return HttpResponse("request data")