from django.db import models


# Create your models here.
class member(models.Model):
    Name = models.CharField(max_length=10, null=False)
    account = models.CharField(max_length=20, null=False, primary_key=True)
    password = models.CharField(max_length=20, null=False)
    date = models.CharField(max_length=20, null=True)
    phone = models.CharField(max_length=20, null=True)
    address = models.CharField(max_length=20, null=True)

    def __str__(self):
       return self.Name
