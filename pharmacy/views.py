from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from items.models import ItemDistribution, Items
from django.http import HttpResponseRedirect
# Create your views here.
@login_required(login_url = "accounts:signin")
def dashboard(request):
    items=ItemDistribution.objects.filter(user=request.user).distinct()
    for i in items:
        filter_item_name=items.filter(item_name=i.item_name)
        print(filter_item_name[0].quantity)
  
    return render(request,"dashboard.html",{"items":items})



@login_required(login_url = "accounts:signin")
def purchase_history(request):
    items=ItemDistribution.objects.filter(user=request.user)
    return render(request,"purchase_history.html",{"items":items})

