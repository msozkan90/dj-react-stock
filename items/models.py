from django.db import models

# Create your models here.
class Items(models.Model):
    item_name=models.CharField(max_length=60)
    quantity=models.CharField(max_length=60)