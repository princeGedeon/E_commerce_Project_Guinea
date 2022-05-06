from django.db import models

# Create your models here.
from user_app.models import Vendeur


class Tags_Products(models.Model):
    libelle=models.CharField(max_length=255)

    def __str__(self):
        return self.libelle
class Categorie(models.Model):
    libelle = models.CharField(max_length=100)
    is_visible=models.BooleanField(default=False)

    def __str__(self):
        return self.libelle

class Product(models.Model):
    libelle=models.CharField(max_length=100)
    image=models.ImageField(upload_to='Products/images')
    desc=models.CharField(max_length=200,blank=True,null=True)
    tags=models.ManyToManyField(Tags_Products)
    category=models.ForeignKey(Categorie,on_delete=models.CASCADE,null=True,default=0)
    price=models.IntegerField()
    etoile=models.IntegerField(default=0)
    size=models.CharField(max_length=20,choices=(('S','S'),('M','M'),('L','L'),('XL','XL'),('No Size','No Size')),default=('No Size','Pas de taille requis'))
    poids=models.FloatField(blank=True,null=True)
    vendeur=models.ForeignKey(Vendeur,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Produit {self.libelle} de {self.vendeur}"

class Stock(models.Model):
    produit=models.ForeignKey(Product,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True)
    quantite_add=models.IntegerField()
    quantite=models.IntegerField()
    total_price=models.IntegerField()


    @property
    def get_vendeur(self):
        return self.produit.vendeur