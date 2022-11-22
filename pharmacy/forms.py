from django import forms
from django.utils.translation import gettext_lazy as _
from .models import PharmacySell
class PharmacySellForm(forms.ModelForm):



    class Meta:
        model = PharmacySell        
        fields = '__all__'
        exclude = ['created_at','updated_at','status']    
        widgets = {

          
            'user': forms.Select(attrs={'class': "form-control form-control-user ",'placeholder':'User',"type":"text",}),
            'item_name': forms.Select(attrs={'class': "form-control form-control-user ",'placeholder':'Malzeme',"type":"text",}),
            'quantity': forms.TextInput(attrs={'class': "form-control form-control-user ", 'placeholder':'Adet',"type":"number" }),
  
        }

        labels = {         
          
            'item_name': _('Malzeme'),
            'user': _('User'),
            'quantity': _('Adet'),

         
        }





class OrderItemForm(forms.ModelForm):



    class Meta:
        model = PharmacySell        
        fields = '__all__'
        exclude = ['created_at','updated_at','status']    
        widgets = {

          
            'user': forms.Select(attrs={'class': "form-control form-control-user ",'placeholder':'User',"type":"text",}),
            'item_name': forms.Select(attrs={'class': "form-control form-control-user ",'placeholder':'Malzeme',"type":"text",}),
            'quantity': forms.TextInput(attrs={'class': "form-control form-control-user ", 'placeholder':'Adet',"type":"number" }),
  
        }

        labels = {         
          
            'item_name': _('Malzeme'),
            'user': _('User'),
            'quantity': _('Adet'),

         
        }

