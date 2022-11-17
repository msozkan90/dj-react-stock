from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from .models import ItemDistribution, Items,PharmacyStorage
from .forms import ItemForm,ItemDistributionForm
from django.http import HttpResponseRedirect
from pharmacy.utils import admin_login_required
import json
# Create your views here.
from django.http import JsonResponse

@admin_login_required(login_url = "accounts:index")
def add_item(request):
    form=ItemForm(request.POST or None )
    if request.method == 'POST':
        if form.is_valid():
                form.save()
                messages.success(request,"Dosya başarılı bir şekilde oluşturuldu.")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    return render(request,"add_item.html",{"form":form})

def add_item_react(request):
    file_array = json.loads(request.body)
    print(file_array)
    #for i in file_array["file_array"]:
    document= Items.objects.create(item_name=file_array["item_name"],status=file_array["status"],quantity=file_array["quantity"])
    print(document)
    return JsonResponse('Documents added..', safe=False)


@admin_login_required(login_url = "accounts:index")
def item_list(request):
    items=Items.objects.all()
    return render(request,"item_list.html",{"items":items})

@admin_login_required(login_url = "accounts:index")
def item_charts(request):
    items=Items.objects.all()
    return render(request,"item_charts.html",{"items":items})


@admin_login_required(login_url = "accounts:index")
def item_distribution(request):
    form=ItemDistributionForm(request.POST or None )

    if request.method == 'POST':
        if form.is_valid():
            user= form.data.get('user')
            quantity= form.data.get('quantity')
            item_name= form.data.get('item_name')
            user_instance=User.objects.filter(id=user).first()
            item_instance=Items.objects.filter(id=item_name).first()
            if int(item_instance.quantity) < int(quantity):
                messages.warning(request,"Stok yeterli değildir.")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
            else:
                form.save()
                storage_check=PharmacyStorage.objects.filter(user=user_instance,item_name=item_instance).count()  
                if storage_check == 0:
                    PharmacyStorage.objects.create(user=user_instance,quantity=quantity,item_name=item_instance)
                    item_instance.quantity = int(item_instance.quantity) - int(quantity)
                    item_instance.save()
                else:
                    storage_update=PharmacyStorage.objects.filter(user=user,item_name=item_instance).first()
                    item_instance.quantity = int(item_instance.quantity) - int(quantity)
                    storage_update.quantity += int(quantity)
                    storage_update.save()
                    item_instance.save()
                messages.success(request,"Malezeme dağıtımı başarılı bir şekilde oluşturuldu.")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    return render(request,"item_distribution.html",{"form":form})

@admin_login_required(login_url = "accounts:index")
def item_distribution_list(request):
    items=ItemDistribution.objects.all()
    return render(request,"item_distribution_list.html",{"items":items})



@admin_login_required(login_url = "accounts:index")
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
