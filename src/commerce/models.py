from django.db import models

# Create your models here.
from user_app.models import Vendeur


class Tags_Products(models.Model):
    libelle=models.CharField(max_length=255)

class Product(models.Model):
    libelle=models.CharField(max_length=100)
    desc=models.CharField(max_length=200,blank=True,null=True)
    tags=models.ManyToManyField(Tags_Products)
    price=models.DecimalField(default=0,max_digits=15,decimal_places=12)
    etoile=models.IntegerField(default=0)
    vendeur=models.ForeignKey(Vendeur,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True)

class Stock(models.Model):
    date=models.DateTimeField(auto_now_add=True)
    quantite_add=models.IntegerField()
    quantite=models.IntegerField()
    total_price=models.DecimalField(max_digits=15,decimal_places=12)


