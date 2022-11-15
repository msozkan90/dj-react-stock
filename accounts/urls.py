from django.contrib import admin
from django.urls import path
from . import views
app_name="accounts"
urlpatterns = [

    path("",views.index,name="index"),
    path("register/",views.register,name="register"),
    path("signin/",views.signin,name="signin"),
]
