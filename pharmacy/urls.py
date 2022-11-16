from django.contrib import admin
from django.urls import path
from . import views
app_name="pharmacy"
urlpatterns = [

    path("dashboard",views.dashboard,name="dashboard"),
    path("purchase/history",views.purchase_history,name="purchase_history"),

]
