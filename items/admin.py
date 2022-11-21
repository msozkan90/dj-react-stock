from django.contrib import admin
from .models import Items,ItemDistribution,PharmacyStorage,Order
# Register your models here.



class ItemAdmin(admin.ModelAdmin):
    list_display = ('item_name', 'quantity')
admin.site.register(Items, ItemAdmin)

class ItemDistributionAdmin(admin.ModelAdmin):
    list_display = ('item_name', 'quantity','user','created_at')
admin.site.register(ItemDistribution, ItemDistributionAdmin)

class PharmacyStorageAdmin(admin.ModelAdmin):
    list_display = ('item_name', 'quantity','user','created_at')
admin.site.register(PharmacyStorage, PharmacyStorageAdmin)



class ItemOrderAdmin(admin.ModelAdmin):
    list_display = ('item_name', 'quantity','user','created_at')
admin.site.register(Order, ItemOrderAdmin)