from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Items
class ItemForm(forms.ModelForm):
    class Meta:
        model = Items        
        fields = '__all__'
        exclude = ['created_at','updated_at']    
        widgets = {

            'item_name': forms.TextInput(attrs={'class': "form-control form-control-user ",'placeholder':'Malzeme Adı',"type":"text",}),
            'quantity': forms.TextInput(attrs={'class': "form-control form-control-user ", 'placeholder':'Adet',"type":"text" }),
            'status': forms.CheckboxInput(attrs={'class': "form-control-user mt-3", 'placeholder':'Durum', }),
        }

        labels = {         
            'item_name': _('Malzeme Adı'),
            'quantity': _('Adet'),
            'status': _('Durum'),
         
        }

        error_messages = {
 
            'item_name': {
                'max_length': _("Dosya no alanı 30 karakterden fazla olamaz."),
                'unique': _("Bu dosya no daha önceden kullanılmış."),
            
            },
            'quantity': {
                'max_length': _("Başvuran alanı 30 karakterden fazla olamaz."),       
                'required':"Lütfen başvuran kısmını doldurunuz."
            },



        }
