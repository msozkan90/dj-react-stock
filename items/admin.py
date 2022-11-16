from django.contrib import admin
from .models import Items,ItemDistribution,PharmacyStorage
# Register your models here.
admin.site.register(Items)
admin.site.register(ItemDistribution)
admin.site.register(PharmacyStorage)