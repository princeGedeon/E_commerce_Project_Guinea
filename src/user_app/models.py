from django.contrib.auth.models import AbstractUser
from django.db import models




# Create your models here.
from django.utils.text import slugify


class User(AbstractUser):
    class Type(models.TextChoices):
        VENDEUR = "VENDEUR", "Vendeur"
        ACHETTEUR = "ACHETTEUR", "Achetteur"
        VISITEUR = "VISITEUR", "Visiteur"
        MEMBER="MEMBRE","Membre"

    couverture= models.ImageField(upload_to="couvertures/images", blank=True, null=True)
    profile = models.ImageField(upload_to="profiles/images", blank=True, null=True)
    email=models.EmailField(unique=True,blank=True)
    phone=models.CharField(max_length=15,blank=True,null=True)
    nationalite=models.CharField(max_length=125,blank=True,null=True)
    bio=models.CharField(max_length=200,blank=True,null=True)
    type=models.CharField(choices=Type.choices,max_length=255,default=Type.VISITEUR)
    is_valid=models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    slug=models.SlugField(max_length=50,blank=True,null=True,unique=True)


    REQUIRED_FIELDS = ['phone','username']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug=slugify(self.username+self.first_name+self.last_name)
        super().save(*args,**kwargs)






    @property
    def date_joined_(self):
        return self.date_joined.date()



class Vendeur(models.Model):
    ville=models.CharField(max_length=150)
    profession=models.CharField(max_length=150,blank=True,null=True)#A revoir
    user=models.OneToOneField(User,on_delete=models.CASCADE,blank=True,null=True,related_name="vendeur")

    def __str__(self):
        return f"{self.user}"

class Achetteur(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE)


class Visiteur(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name="visiteur")

class Member(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    poste=models.CharField(max_length=150,blank=True,null=True)


    def __str__(self):
        return f"Membre {self.user.username}"





