from django.db import models


# Create your models here.
class member(models.Model):

    Name = models.CharField(max_length=10, null=False)
    account = models.CharField(max_length=20, null=False,unique="True")
    password = models.CharField(max_length=20, null=False)
    email = models.EmailField(max_length=100, null=False)
    date = models.CharField(max_length=20, null=True,blank=True,default='')
    phone = models.CharField(max_length=10, null=True,blank=True,default='')
    address = models.CharField(max_length=49, null=True,blank=True,default='')

    def __str__(self):
       return self.Name


