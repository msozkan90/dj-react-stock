from django.contrib import admin
from django.urls import path
from . import views
app_name="pharmacy"
urlpatterns = [
    path("getItemList",views.getItemList,name="getItemList"),
    path("dashboard",views.dashboard,name="dashboard"),
    path("purchase/history",views.purchase_history,name="purchase_history"),
    path("sell/history",views.sell_history,name="sell_history"),
    path("order/history",views.order_history,name="order_history"),
    path("sell/item",views.sell_item,name="sell_item"),
    path("order/item/react",views.order_item_react,name="order_item_react"),
    path("order/item",views.order_item,name="order_item"),
    path("orders",views.orders,name="orders"),
    path("sell/item/react",views.sell_item_react,name="sell_item_react"),


]
