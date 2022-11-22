from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Items(models.Model):
    item_name=models.CharField(max_length=60)
    quantity=models.DecimalField(max_digits=10,decimal_places=2)
    status=models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated_at = models.DateTimeField(auto_now=True,null=True,blank=True)
    def __str__(self):
        return self.item_name




class ItemDistribution(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    item_name = models.ForeignKey(Items, on_delete=models.SET_NULL,null=True)
    quantity=models.DecimalField(max_digits=10,decimal_places=2)
    status=models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated_at = models.DateTimeField(auto_now=True,null=True,blank=True)
    def __str__(self):
        return self.item_name.item_name,self.user.username


class PharmacyStorage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item_name = models.ForeignKey(Items, on_delete=models.SET_NULL,null=True)
    quantity=models.DecimalField(max_digits=10,decimal_places=2)
    status=models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated_at = models.DateTimeField(auto_now=True,null=True,blank=True)
    def __str__(self):
        return self.item_name.item_name



class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item_name = models.ForeignKey(Items, on_delete=models.SET_NULL,null=True)
    quantity=models.DecimalField(max_digits=10,decimal_places=2)
    status=models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated_at = models.DateTimeField(auto_now=True,null=True,blank=True)
    def __str__(self):
        return self.item_name.item_name