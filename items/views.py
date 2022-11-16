from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from .models import ItemDistribution, Items
from .forms import ItemForm,ItemDistributionForm
from django.http import HttpResponseRedirect
# Create your views here.


@login_required(login_url = "accounts:signin")
def add_item(request):
    form=ItemForm(request.POST or None )
    if request.method == 'POST':
        print(form.errors)
        if form.is_valid():
                form.save()
                messages.success(request,"Dosya başarılı bir şekilde oluşturuldu.")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    return render(request,"add_item.html",{"form":form})



@login_required(login_url = "accounts:signin")
def item_list(request):
    items=Items.objects.all()
    return render(request,"item_list.html",{"items":items})

@login_required(login_url = "accounts:signin")
def item_charts(request):
    items=Items.objects.all()
    return render(request,"item_charts.html",{"items":items})


@login_required(login_url = "accounts:signin")
def item_distribution(request):
    form=ItemDistributionForm(request.POST or None )
    if request.method == 'POST':
        if form.is_valid():
                form.save()
                messages.success(request,"Malezeme dağıtımı başarılı bir şekilde oluşturuldu.")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    return render(request,"item_distribution.html",{"form":form})

@login_required(login_url = "accounts:signin")
def item_distribution_list(request):
    items=ItemDistribution.objects.all()
    return render(request,"item_distribution_list.html",{"items":items})



@login_required(login_url = "accounts:signin")
def edit_item(request,pk):
    instance = get_object_or_404(Items,id = pk)
    form=ItemForm(request.POST or None,instance = instance)
    if request.method == 'POST':
        print(form.errors)
        if form.is_valid():
                form.save()
                messages.success(request,"Dosya başarılı bir şekilde oluşturuldu.")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    return render(request,"edit_item.html",{"form":form})
