from django.contrib import admin
from django.urls import path, include
from .views import index,ReviewAPI,testview
urlpatterns = [
    path('index/',index,name="index"),
    path('review/',ReviewAPI,name='review'),
    path('testview/',testview.as_view(),name='test_view')
]