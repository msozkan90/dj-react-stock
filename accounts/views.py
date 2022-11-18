from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponseRedirect
from accounts.models import UserProfile
from .forms import CreateUserForm,LoginUserForm, UpdateUserForm,UserProfileForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from pharmacy.utils import admin_login_required
import json
from django.http import JsonResponse

def index(request):
    return render(request,"index.html")


def signin(request):
    form=LoginUserForm()
    if request.method == 'POST':
        username = request.POST.get('username')
        password =request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        username_check=User.objects.filter(username=username)
        if user is not None:
            login(request, user)
            messages.success(request, 'You logged in successfully')
            return redirect('accounts:index')
        elif(not username_check):
            messages.warning(request, 'Username incorrect ')
            return redirect('accounts:signin')
        else:
            messages.warning(request, 'Password incorrect ')
            context = {"form":form}
            return redirect('accounts:signin')
    context = {"form":form}
    return render(request,"signin.html",context)

@admin_login_required(login_url = "accounts:index")
def pharmacy_list(request):
    pharmacys=User.objects.all()
    return render(request,"pharmacy_list.html",{"pharmacys":pharmacys})


@admin_login_required(login_url = "accounts:index")
def add_pharmacy(request):
    form=CreateUserForm()
    form_profile=UserProfileForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        form_profile=UserProfileForm(request.POST)
        password1= form.data.get('password1')
        password2= form.data.get('password2')
        username= form.data.get('username')
        email = form.data.get('email')
        pharmacy_name = form.data.get('pharmacy_name')
        address = form.data.get('address')
        email_check=User.objects.filter(email=email)
        users=User.objects.filter(username=username)
        try:
            if form.is_valid and form_profile.is_valid:
                    user = form.save(commit=False)
                    user.save()
                    user.userprofile.pharmacy_name=pharmacy_name
                    user.userprofile.address=address
                    user.save()
                    messages.success(request,"Eczane başarılı bir şekilde eklendi.")
                    return redirect("accounts:pharmacy_list")
        except(ValueError):
            if(password1 != password2):
                    messages.warning(request,"Passwords did not match")
                    return redirect("accounts:add_pharmacy")
            if(users):
                messages.warning(request,"This user name is already taken")
                return redirect("accounts:add_pharmacy")
            if(email_check):
                    messages.warning(request,"This email is already taken")
                    return redirect("accounts:add_pharmacy")
    return render(request,"add_pharmacy.html",{"form":form,"form_profile":form_profile})

def add_pharmacy_react(request):
 
    file_array = json.loads(request.body)
    password1= file_array['password1']
    password2= file_array['password2']
    username= file_array['username']
    email = file_array['email']
    pharmacy_name = file_array['pharmacy_name']
    address = file_array['address']
    email_check=User.objects.filter(email=email)
    users=User.objects.filter(username=username)
    try:
        if(password1 != password2):
             
                return JsonResponse({"message":"Passwords did not match.","color":"#f34444","type":"Başarısız"}, safe=False)
        if(users):
        
            return JsonResponse({"message":"This user name is already taken.","color":"#f34444","type":"Başarısız"}, safe=False)
        if(email_check):
           
                return JsonResponse({"message":"This email is already taken.","color":"#f34444","type":"Başarısız"}, safe=False)
        user=User.objects.create(username=username,password=password1,email=email)
        user.save()
        user.userprofile.pharmacy_name=pharmacy_name
        user.userprofile.address=address
        user.save()
        user.userprofile.save()
        return JsonResponse({"message":"Dağıtım başarılı bir şekilde oluşturuldu.","color":"#89D99D","type":"Başarılı"}, safe=False)

    except(ValueError):
        if(password1 != password2):
             
                return JsonResponse({"message":"Passwords did not match.","color":"#f34444","type":"Başarısız"}, safe=False)
        if(users):
        
            return JsonResponse({"message":"This user name is already taken.","color":"#f34444","type":"Başarısız"}, safe=False)
        if(email_check):
           
                return JsonResponse({"message":"This email is already taken.","color":"#f34444","type":"Başarısız"}, safe=False)


@admin_login_required(login_url = "accounts:index")
def edit_pharmacy(request,pk):
    instance = get_object_or_404(User,id = pk)
    instance_profile = get_object_or_404(UserProfile,user = instance)
    form=UpdateUserForm(request.POST or None,instance = instance)
    form_profile=UserProfileForm(request.POST or None,instance = instance_profile)
    if request.method == 'POST':
        print(form_profile.errors)
        print(form.errors)
        if form.is_valid and form_profile.is_valid:

            form.save()
            form_profile.save()
            messages.success(request,"Eczane başarılı bir şekilde güncellendi.")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    return render(request,"edit_pharmacy.html",{"form":form,"form_profile":form_profile})














def register(request):
    form=CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        password1= form.data.get('password1')
        password2= form.data.get('password2')
        username= form.data.get('username')
        email = form.data.get('email')
        email_check=User.objects.filter(email=email)
        users=User.objects.filter(username=username)
        try:
            if form.is_valid:
                    user = form.save(commit=False)
                    user.save()
                    messages.success(request,"You registered successfully. Please log in.")
                    return redirect("accounts:signin")
        except(ValueError):
            if(password1 != password2):
                    messages.warning(request,"Passwords did not match")
                    return redirect("accounts:register")
            if(users):
                messages.warning(request,"This user name is already taken")
                return redirect("accounts:register")
            if(email_check):
                    messages.warning(request,"This email is already taken")
                    return redirect("user:register")
    return render(request,"register.html",{"form":form})


def log_out(request):
	logout(request)
	messages.success(request, "Oturumu başarılı bir şekilde sonlandırdınız.")
	return redirect("../signin")
