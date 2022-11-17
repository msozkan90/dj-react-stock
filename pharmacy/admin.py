from django.contrib import admin
from .models import PharmacySell
# Register your models here.

class PharmacySellAdmin(admin.ModelAdmin):
    list_display = ('item_name', 'quantity','user','created_at')
admin.site.register(PharmacySell, PharmacySellAdmin)