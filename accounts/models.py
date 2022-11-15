
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
import os
from django.db import connection
from django.utils.crypto import get_random_string

# Create your models here.
User._meta.get_field('email').blank = False
User._meta.get_field('email')._unique = True

def update_filename(instance, filename):
    basefilename, file_extension= os.path.splitext(filename)
    tenant = connection.get_tenant()
    file_name= get_random_string(length=20)
    filename= str(file_name + file_extension)
    path = "profile_photos\\" + str(tenant)
    format = filename
    return os.path.join(path, format)

class LoggedInUser(models.Model):
    user = models.OneToOneField(User, related_name='logged_in_user', on_delete=models.CASCADE)
    # Session keys are 32 characters long
    session_key = models.CharField(max_length=32, null=True, blank=True)
    def __str__(self):
        return self.user.username

STATUS = (
        (1,  _('Admin')),
        (2, _('Müşteri')),


    )
GENDER = (
        (1,  _('Erkek')),
        (2, _('Kadın')),

    )

class Company(models.Model):
    company = models.CharField(max_length=100)
    status = models.PositiveSmallIntegerField(
        choices=STATUS,
        default=1,  
    )
    def __str__(self):
        return self.company
 
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.ForeignKey(Company, on_delete=models.CASCADE)
    status = models.PositiveSmallIntegerField(
        choices=STATUS,
        default=1,  
    )

    phone = models.CharField(max_length=11,null=True, blank=True)
    gender=models.PositiveSmallIntegerField(
        choices=GENDER,
        null=True, blank=True
    )
    registration_number=models.CharField(max_length=15,null=True, blank=True)
    identity_number=models.CharField(max_length=11,null=True, blank=True)
    birthdate=models.DateField(null=True, blank=True)
    address = models.CharField(max_length=300,null=True, blank=True)
    def __str__(self):
        return self.user.username
