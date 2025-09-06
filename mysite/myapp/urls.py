from django.contrib import admin
from django.urls import path, include
from .views import index,ReviewAPI,testview,detailview
app_name="myapp"
urlpatterns = [
    path('',index,name="index"),
    path('review/',ReviewAPI,name='review'),
    path('testview/',testview.as_view(),name='test_view'),
    path('<int:id>/',detailview,name="detail_view"),
]