from django.shortcuts import render,redirect
from .forms import CreateUserForm   
from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.
def index(request):
    return render(request,"index.html")


def signin(request):

    return render(request,"signin.html")



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