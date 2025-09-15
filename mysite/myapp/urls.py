from django.contrib import admin
from django.urls import path, include
from .views import index,ReviewAPI,testview,detailview,create_item, update_item,delete_item
app_name="myapp"
urlpatterns = [
    path('',index,name="index"),
    path('review/',ReviewAPI,name='review'),
    path('testview/',testview.as_view(),name='test_view'),
    path('<int:id>/',detailview,name="detail_view"),
    path('add/',create_item,name="create_item"),
    path('update/<int:id>/',update_item,name="update_item"),
    path('delete/<int:id>/',delete_item,name="delete_item"),
]