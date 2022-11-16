from django.contrib import admin
from django.urls import path
from . import views
app_name="accounts"
urlpatterns = [

    path("",views.index,name="index"),
    path("register/",views.register,name="register"),
    path("signin/",views.signin,name="signin"),
    path("logout/",views.log_out,name="logout"),
    path("add/pharmacy",views.add_pharmacy,name="add_pharmacy"),
    path("pharmacy/list",views.pharmacy_list,name="pharmacy_list"),
    path("edit/pharmacy/<int:pk>/",views.edit_pharmacy,name="edit_pharmacy"),

    
]
