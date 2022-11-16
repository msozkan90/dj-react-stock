from django import forms
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from accounts.models import  UserProfile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import AuthenticationForm
class SetPasswordForm(forms.Form):
    new_password1 = forms.CharField(
        label=_("New password"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        strip=False,
    )
    new_password2 = forms.CharField(
        label=_("New password confirmation"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
    )
def validate_email(value):
    if User.objects.filter(email = value).exists():
        raise ValidationError((f"{value} is taken."),params = {'value':value})


class CreateUserForm(UserCreationForm):
    email = forms.CharField(validators = [validate_email],widget=forms.EmailInput(attrs={'class': "form-control form-control-user", 'placeholder':'Email',"max":"40","type":"email", }),label=  _('Email'))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': "form-control form-control-user", 'placeholder':'Password',"type":"password", }),label=  _('Password'))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': "form-control form-control-user", 'placeholder':'Password Confirmation',"type":"password", }),label=  _('Password Confirmation'))
    class Meta:
        model = User
        
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {

            'username': forms.TextInput(attrs={'class': "form-control form-control-user",'placeholder':'Username',"type":"text",}),
            'email': forms.TextInput(attrs={'class': "form-control form-control-user ", 'placeholder':'Email',"type":"email" }),
            'password1': forms.TextInput(attrs={'class': "form-control form-control-user",'placeholder':'Password',"type":"password"}),
            'password2': forms.TextInput(attrs={'class': "form-control form-control-user", 'placeholder':'Password Confirmation',"type":"password"}),
        }       
        labels = {       
            'username': _('Username'),
            'email': _('Email'),
            'password1': _('Password'),
            'password2': _('Password Confirmation'),
        }  





class LoginUserForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control form-control-user", 'placeholder':'Username',"type":"text", }),label=  _('Username'))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': "form-control form-control-user", 'placeholder':'Password',"type":"password", }),label=  _('Password'))

    class Meta:
        model = User
        
        fields = ['username', 'password']
        widgets = {


        }       
        labels = {       
            'username': _('Username'),
            'password': _('Password'),
   
        }  


class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control form-control-user mb-2', 'placeholder':'Username',"type":"text",}))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control form-control-user mb-2', 'placeholder':'Email',"type":"email",}))

    class Meta:
        model = User
        fields = ['username', 'email']

class UserProfileForm(forms.ModelForm):
    pharmacy_name=forms.CharField(required=True,widget=forms.TextInput(attrs={'class': "form-control form-control-user mb-2  ",'placeholder':'Eczane Adı','type':"text"}),label=  _('Eczane Adı') )

    class Meta:
        model = UserProfile        
        fields = '__all__'
        exclude = ['user','status']
        widgets = {

            'address': forms.Textarea(attrs={'class': "form-control form-control-user mb-2 ", 'placeholder':'Adres',"cols":"10","rows":"7" }),
        }       
        labels = {       
            'pharmacy_name': _('Eczane Adı'),
            'address': _('Adres'),
        }       
        error_messages = {
            'pharmacy_name': {
                'max_length': _("This phone is too long."),
                'unique': _("This phone is already taken."),
                'required':"Please Enter your phone"
            },

            'address': {
                'max_length': _("This address is too long."),
                'unique': _("This address is already taken."),
                'required':"Please Enter your address"
            },

        }