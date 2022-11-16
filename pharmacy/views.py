from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from items.models import ItemDistribution, Items,PharmacyStorage
from django.http import HttpResponseRedirect

from pharmacy.models import PharmacySell
# Create your views here.
@login_required(login_url = "accounts:signin")
def dashboard(request):
    items=PharmacyStorage.objects.filter(user=request.user)
    return render(request,"dashboard.html",{"items":items})



@login_required(login_url = "accounts:signin")
def purchase_history(request):
    items=ItemDistribution.objects.filter(user=request.user)
    return render(request,"purchase_history.html",{"items":items})


@login_required(login_url = "accounts:signin")
def sell_history(request):
    items=PharmacySell.objects.filter(user=request.user)
    return render(request,"sell_history.html",{"items":items})

@login_required(login_url = "accounts:signin")
def sell_item(request):
    items=PharmacySell.objects.filter(user=request.user)
    return render(request,"sell_item.html",{"items":items})
