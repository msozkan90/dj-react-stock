from django.contrib import admin
from django.urls import path
from . import views
app_name="items"
urlpatterns = [

    path("items",views.item_list,name="item_list"),
    path("add/item",views.add_item,name="add_item"),

]
