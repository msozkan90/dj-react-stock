from django.contrib import admin
from django.urls import path
from . import views
app_name="items"
urlpatterns = [

    path("items",views.item_list,name="item_list"),
    path("add/item",views.add_item,name="add_item"),

    path("add/item/react",views.add_item_react,name="add_item_react"),
    path("item/distribution/react",views.item_distribution_react,name="item_distribution_react"),


    path("item/charts",views.item_charts,name="item_charts"),
    path("item/distribution",views.item_distribution,name="item_distribution"),
    path("item/distribution/list",views.item_distribution_list,name="item_distribution_list"),
    path("edit/item/<int:pk>/",views.edit_item,name="edit_item"),
    path("getUserList",views.getUserList,name="getUserList"),

]
