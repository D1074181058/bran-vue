from django.db import models


# Create your models here.
class member(models.Model):

    Name = models.CharField(max_length=10, null=False)
    account = models.CharField(max_length=20, null=False,unique="True")
    password = models.CharField(max_length=20, null=False)
    email = models.EmailField(max_length=100, null=False,unique="True")
    date = models.CharField(max_length=20, null=True,blank=True,default='')
    phone = models.CharField(max_length=10, null=True,blank=True,default='')
    address = models.CharField(max_length=49, null=True,blank=True,default='')

    def __str__(self):
       return self.account

class NewsUnit(models.Model):
    catego = models.CharField(max_length=10, null=False)
    nickname = models.CharField(max_length=20, null=False)
    title = models.CharField(max_length=50, null=False)
    message = models.TextField(null=False)
    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Order(models.Model):
    customname = models.CharField(max_length=20)
    customaccount = models.CharField(max_length=20)
    customemail = models.EmailField(max_length=60, default='',null=True)
    customphone=models.CharField(max_length=15,default='',null=True)
    customaddress = models.CharField(max_length=100, default='',null=True)
    unitname = models.CharField(max_length=100,default='')
    unitnum=models.IntegerField(default=0)
    unitprice=models.IntegerField(default=0)
    nowtime = models.CharField(max_length=50)
    def __str__(self):
        return self.customname
class Orderview(models.Model):
    customname = models.CharField(max_length=20)
    customaccount = models.CharField(max_length=20)
    salename = models.CharField(max_length=20)
    salenum = models.IntegerField(default=0)
    saleprice = models.IntegerField(default=0)
    def __str__(self):
        return self.customname


class beefview(models.Model):
    salename = models.CharField(max_length=20)
    saleprice = models.IntegerField(default=0)
    imgname = models.CharField(max_length=20)
    def __str__(self):
        return self.salename
class pigview(models.Model):
    salename = models.CharField(max_length=20)
    saleprice = models.IntegerField(default=0)
    imgname = models.CharField(max_length=20)
    def __str__(self):
        return self.salename
class chickenview(models.Model):
    salename = models.CharField(max_length=20)
    saleprice = models.IntegerField(default=0)
    imgname = models.CharField(max_length=20)
    def __str__(self):
        return self.salename
class lambview(models.Model):
    salename = models.CharField(max_length=20)
    saleprice = models.IntegerField(default=0)
    imgname = models.CharField(max_length=20)
    def __str__(self):
        return self.salename
class agaricusview(models.Model):
    salename = models.CharField(max_length=20)
    saleprice = models.IntegerField(default=0)
    imgname = models.CharField(max_length=20)
    def __str__(self):
        return self.salename
class seafoodview(models.Model):
    salename = models.CharField(max_length=20)
    saleprice = models.IntegerField(default=0)
    imgname = models.CharField(max_length=20)
    def __str__(self):
        return self.salename
class vegetableview(models.Model):
    salename = models.CharField(max_length=20)
    saleprice = models.IntegerField(default=0)
    imgname = models.CharField(max_length=20)
    def __str__(self):
        return self.salename






