from django.db import models
from django.contrib.auth.models import User
from items.models import Items
# Create your models here.



class PharmacySell(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item_name = models.ForeignKey(Items, on_delete=models.SET_NULL,null=True)
    quantity=models.DecimalField(max_digits=10,decimal_places=2)
    status=models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated_at = models.DateTimeField(auto_now=True,null=True,blank=True)
    def __str__(self):
        return self.item_name.item_name,self.user.username

