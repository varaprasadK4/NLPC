from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
class signup(models.Model):
     Name = models.CharField(max_length=100,default='none')
     Email = models.EmailField(max_length=100,default='none')
     Number = PhoneNumberField(blank="False",primary_key="true")
     password = models.CharField(max_length=100,null="False",blank="False",default="None")
     c_password = models.CharField(max_length=100,null="False",blank="False",default="None")





