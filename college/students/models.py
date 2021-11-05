from django.db import models

from django_countries.fields import CountryField
# Create your models here.
class Studentdata(models.Model):
    M='Male'
    F='Female'
    Genderchoices=[(M, 'Male'),(F, 'Female')]

    name=models.CharField(max_length=15,null=True)
    Regid=models.IntegerField(null=True)
    email=models.EmailField(null=True)
    password=models.CharField(max_length=15,null=True)
    address=models.TextField(null=True)
    country=CountryField(blank_label='select country')
    gender=models.CharField(max_length=15, choices=Genderchoices)
    Markspersentage=models.FloatField(null=True)





