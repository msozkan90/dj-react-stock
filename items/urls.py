from django.contrib import admin
from django.urls import path
from . import views
app_name="items"
urlpatterns = [

    path("items",views.item_list,name="item_list"),
    path("add/item",views.add_item,name="add_item"),
    path("item/charts",views.item_charts,name="item_charts"),
    path("item/distribution",views.item_distribution,name="item_distribution"),
    path("item/distribution/list",views.item_distribution_list,name="item_distribution_list"),
    path("edit/item/<int:pk>/",views.edit_item,name="edit_item"),

]
