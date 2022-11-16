from django.db import models

# Create your models here.
class Items(models.Model):
    item_name=models.CharField(max_length=60)
    quantity=models.CharField(max_length=60)
    status=models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated_at = models.DateTimeField(auto_now=True,null=True,blank=True)
    def __str__(self):
        return self.item_name