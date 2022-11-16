from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from .models import Items
# Create your views here.


@login_required(login_url = "accounts:signin")
def add_item(request):
    return render(request,"add_item.html")



@login_required(login_url = "accounts:signin")
def item_list(request):
    items=Items.objects.all()
    return render(request,"item_list.html",{"items":items})

