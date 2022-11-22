from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from accounts.models import UserProfile
from items.models import ItemDistribution, Items, Order,PharmacyStorage
from django.http import HttpResponseRedirect
from pharmacy.forms import PharmacySellForm,OrderItemForm
from .utils import admin_login_required
from pharmacy.models import PharmacySell
import json
from django.http import JsonResponse
@login_required(login_url = "accounts:signin")
def dashboard(request):
    if request.user.userprofile.status == 1:
        items=Items.objects.all()
        return render(request,"dashboard.html",{"items":items})
    else:
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


def getItemList(request):
    items=list(Items.objects.values())
    return JsonResponse( items, safe=False)



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

def sell_item_react(request):
    file_array = json.loads(request.body)

    item_instance=Items.objects.filter(id=file_array["item_name"]).first()

    user_instance=User.objects.filter(id=file_array["user"]["id"]).first()

    pharmacy_storage=PharmacyStorage.objects.filter(user=user_instance,item_name=item_instance).first()    
    try:
        if int(pharmacy_storage.quantity) < int(file_array["quantity"]):
            return JsonResponse({"message":"Stok yeterli değildir.","color":"#f34444","type":"Başarısız"}, safe=False)
        else:
            document= PharmacySell.objects.create(user=user_instance,item_name=item_instance,quantity=file_array["quantity"])        
            pharmacy_storage.quantity = int(pharmacy_storage.quantity) - int(file_array["quantity"])
            pharmacy_storage.save()
            # messages.success(request,"Satış başarılı bir şekilde oluşturuldu.")
            return JsonResponse({"message":"Satış başarılı bir şekilde oluşturuldu.","color":"#89D99D","type":"Başarılı"}, safe=False)
    except:
        return JsonResponse({"message":"Stokta bu ürün yok.","color":"#f34444","type":"Başarısız"}, safe=False)

    

@login_required(login_url = "accounts:signin")
def order_item(request):
    form=OrderItemForm(request.POST or None )
    form.user=request.user
    return render(request,"order_item.html",{"form":form})


def order_item_react(request):
    file_array = json.loads(request.body)
    user_instance=User.objects.filter(id=file_array["user"]["id"]).first()
    item_instance=Items.objects.filter(id=file_array["item_name"]).first()
    document= Order.objects.create(item_name=item_instance,user=user_instance,quantity=file_array["quantity"])
    return JsonResponse({"message":"Sipariş başarılı bir şekilde oluşturuldu.","color":"#89D99D","type":"Başarılı"}, safe=False)



@login_required(login_url = "accounts:signin")
def order_history(request):
    items=Order.objects.filter(user=request.user)
    return render(request,"order_history.html",{"items":items})


@admin_login_required(login_url = "pharmacy:dashboard")
def orders(request):
    items=Order.objects.values()
    return render(request,"orders.html",{"items":items})

def getOrderList(request):

    orders=list(Order.objects.values())
    return JsonResponse( orders, safe=False)

def getUsername(request,id):

    username=User.objects.filter(id=id).first()
    return JsonResponse( username.username, safe=False)

def getUserprofile(request,id):

    username=User.objects.filter(id=id).first()
    userprofile=UserProfile.objects.filter(user=username).first()
    return JsonResponse( userprofile.pharmacy_name, safe=False)

def delete_pharmacy_react(request,id):
    username=User.objects.filter(id=id).first()
    # userprofile=UserProfile.objects.filter(user=username).first()
    # userprofile.delete()
    username.delete()
    return JsonResponse({"message":"Eczane başarılı bir şekilde silindi.","color":"#89D99D","type":"Başarılı"}, safe=False)


def getItemname(request,id):
    itemname=Items.objects.filter(id=id).first()
    return JsonResponse( itemname.item_name, safe=False)






def confirm_order_react(request,id):
    file_array = json.loads(request.body)
    order=Order.objects.filter(id=file_array["id"]).first()
    item=Items.objects.filter(item_name=order.item_name).first()
    user_instance=order.user
    print(order.quantity)
    print(item.quantity)

    if int(item.quantity) < int(order.quantity):
        print("burda")
        return JsonResponse({"message":"Stok yeterli değildir.","color":"#f34444","type":"Başarısız"}, safe=False)
    else:
        storage_check=PharmacyStorage.objects.filter(user=user_instance,item_name=item).count()  
        if storage_check == 0:
            PharmacyStorage.objects.create(user=user_instance,quantity=order.quantity,item_name=item)
            item.quantity = int(item.quantity) - int(order.quantity)
            item.save()
            order.status=True
            order.save()
            ItemDistribution.objects.create(user=user_instance,item_name=item,quantity=order.quantity)
            return JsonResponse({"message":"Dağıtım başarılı bir şekilde oluşturuldu.","color":"#89D99D","type":"Başarılı"}, safe=False)
        else:
            storage_update=PharmacyStorage.objects.filter(user=user_instance,item_name=item).first()
            item.quantity = int(item.quantity) - int(order.quantity)
            storage_update.quantity += int(order.quantity)
            storage_update.save()
            item.save()
            order.status=True
            order.save()
            ItemDistribution.objects.create(user=user_instance,item_name=item,quantity=order.quantity)
            return JsonResponse({"message":"Dağıtım başarılı bir şekilde oluşturuldu.","color":"#89D99D","type":"Başarılı"}, safe=False)

