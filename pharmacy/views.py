from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from items.models import ItemDistribution, Items,PharmacyStorage
from django.http import HttpResponseRedirect
from pharmacy.forms import PharmacySellForm
from .utils import admin_login_required
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
    form=PharmacySellForm(request.POST or None )
    form.user=request.user
    if request.method == 'POST':
        print(form.errors)
        if form.is_valid():
            user=request.user           
            quantity= form.data.get('quantity')
            item_name= form.data.get('item_name')
            # user_instance=User.objects.filter(id=user).first()
            item_instance=Items.objects.filter(id=item_name).first()
            try:
                pharmacy_storage=PharmacyStorage.objects.filter(user=user,item_name=item_instance).first()
                if int(pharmacy_storage.quantity) < int(quantity):
                    messages.warning(request,"Stok yeterli değildir.")
                    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
                else:
                    form.save()
                    pharmacy_storage.quantity = int(pharmacy_storage.quantity) - int(quantity)
                    pharmacy_storage.save()
                    messages.success(request,"Satış başarılı bir şekilde oluşturuldu.")
                    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
            except:
                messages.warning(request,"Stokta bu ürün yok.")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

    return render(request,"sell_item.html",{"form":form})
