from django.shortcuts import render,get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
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
                messages.success(request,"Malzeme başarılı bir şekilde oluşturuldu.")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    return render(request,"add_item.html",{"form":form})

def add_item_react(request):
    file_array = json.loads(request.body)
    document= Items.objects.create(item_name=file_array["item_name"],status=file_array["status"],quantity=file_array["quantity"])
    return JsonResponse({"message":"Malzeme başarılı bir şekilde oluşturuldu.","color":"#89D99D","type":"Başarılı"}, safe=False)


def getUserList(request):
    users=list(User.objects.filter(is_superuser=False).values())
    return JsonResponse( users, safe=False)



def delete_item_react(request,id):
    item=Items.objects.filter(id=id).first()
    item.delete()
    return JsonResponse({"message":"Malzeme başarılı bir şekilde silindi.","color":"#89D99D","type":"Başarılı"}, safe=False)


def item_distribution_react(request):
    file_array = json.loads(request.body)
    user= file_array["user"]
    quantity= file_array["quantity"]
    item_name= file_array["item_name"]
    user_instance=User.objects.filter(id=user).first()
    item_instance=Items.objects.filter(id=item_name).first()
    if int(item_instance.quantity) < int(quantity):

        return JsonResponse({"message":"Stok yeterli değildir.","color":"#f34444","type":"Başarısız"}, safe=False)
    else:
        storage_check=PharmacyStorage.objects.filter(user=user_instance,item_name=item_instance).count()  
        if storage_check == 0:
            PharmacyStorage.objects.create(user=user_instance,quantity=quantity,item_name=item_instance)
            item_instance.quantity = int(item_instance.quantity) - int(quantity)
            item_instance.save()
            ItemDistribution.objects.create(user=user_instance,item_name=item_instance,quantity=quantity)
            return JsonResponse({"message":"Dağıtım başarılı bir şekilde oluşturuldu.","color":"#89D99D","type":"Başarılı"}, safe=False)
        else:
            storage_update=PharmacyStorage.objects.filter(user=user,item_name=item_instance).first()
            item_instance.quantity = int(item_instance.quantity) - int(quantity)
            storage_update.quantity += int(quantity)
            storage_update.save()
            item_instance.save()
            ItemDistribution.objects.create(user=user_instance,item_name=item_instance,quantity=quantity)
        return JsonResponse({"message":"Dağıtım başarılı bir şekilde oluşturuldu.","color":"#89D99D","type":"Başarılı"}, safe=False)




@admin_login_required(login_url = "pharmacy:dashboard")
def item_list(request):
    items=Items.objects.all()
    return render(request,"item_list.html",{"items":items})

@admin_login_required(login_url = "pharmacy:dashboard")
def item_charts(request):
    items=Items.objects.all()
    return render(request,"item_charts.html",{"items":items})


@admin_login_required(login_url = "pharmacy:dashboard")
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
                    ItemDistribution.objects.create(user=user_instance,item_name=item_instance,quantity=quantity)
                else:
                    storage_update=PharmacyStorage.objects.filter(user=user,item_name=item_instance).first()
                    item_instance.quantity = int(item_instance.quantity) - int(quantity)
                    storage_update.quantity += int(quantity)
                    storage_update.save()
                    item_instance.save()
                    ItemDistribution.objects.create(user=user_instance,item_name=item_instance,quantity=quantity)
                messages.success(request,"Malzeme dağıtımı başarılı bir şekilde oluşturuldu.")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    return render(request,"item_distribution.html",{"form":form})

@admin_login_required(login_url = "pharmacy:dashboard")
def item_distribution_list(request):
    items=ItemDistribution.objects.all()
    return render(request,"item_distribution_list.html",{"items":items})



@admin_login_required(login_url = "pharmacy:dashboard")
def edit_item(request,pk):
    instance = get_object_or_404(Items,id = pk)
    form=ItemForm(request.POST or None,instance = instance)
    if request.method == 'POST':
        if form.is_valid():
                form.save()
                messages.success(request,"Malzeme başarılı bir şekilde düzenlendi.")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    return render(request,"edit_item.html",{"form":form,"instance":instance})




def edit_item_react(request,pk):
    file_array = json.loads(request.body)
    item=Items.objects.filter(id=pk).first()
    item_name= file_array['item_name']
    quantity= file_array['quantity']
    status= file_array['status']
    item.item_name=item_name
    item.quantity=quantity
    item.status=status
    item.save()
    return JsonResponse({"message":"Malzeme başarılı bir şekilde düzenlendi.","color":"#89D99D","type":"Başarılı"}, safe=False)




def getItem(request,id):
    users=list(User.objects.values())
    return JsonResponse( users, safe=False)


