
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class mobileCustamisation(models.Model):
    brand=models.CharField(max_length=20)
    size_of_screen=models.CharField(max_length=20)
    proceseor=models.CharField(max_length=20)
    ram=models.CharField(max_length=20)
    camera=models.CharField(max_length=20)
    customorID=models.IntegerField()



class buy (models.Model):
    customorID=models.IntegerField()
    productID=models.IntegerField()
    prise=models.IntegerField(default=1)
    Address=models.CharField(max_length=20, default="not address contact by email")
 

