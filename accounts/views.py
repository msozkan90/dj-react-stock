from django.shortcuts import render,redirect
from .forms import CreateUserForm,LoginUserForm 
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url = "accounts:signin")
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
