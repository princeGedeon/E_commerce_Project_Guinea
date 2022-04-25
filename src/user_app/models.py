from django.contrib.auth.models import AbstractUser
from django.db import models




# Create your models here.
class User(AbstractUser):
    class Type(models.TextChoices):
        VENDEUR = "VENDEUR", "Vendeur"
        ACHETTEUR = "ACHETTEUR", "Achetteur"
        VISITEUR = "VISITEUR", "Visiteur"
        MEMBER="MEMBRE","Membre"


    email=models.EmailField(unique=True,blank=True)
    phone=models.CharField(max_length=15)
    nationalite=models.CharField(max_length=125)
    type=models.CharField(choices=Type.choices,max_length=255,default=Type.VISITEUR)
    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['phone','username']






    @property
    def date_joined_(self):
        return self.date_joined.date()



class Vendeur(models.Model):
    profile=models.ImageField(upload_to="profiles/Vendeur/images",blank=True,null=True)
    bio=models.CharField(max_length=200,blank=True,null=True)
    profession=models.CharField(max_length=150,blank=True,null=True)#A revoir
    user=models.OneToOneField(User,on_delete=models.CASCADE,blank=True,null=True)

    def __str__(self):
        return f"{self.user}"

class Achetteur(models.Model):
    profile = models.ImageField(upload_to="profiles/Vendeur/images",blank=True,null=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE)

class Member(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    poste=models.CharField(max_length=150,blank=True,null=True)





