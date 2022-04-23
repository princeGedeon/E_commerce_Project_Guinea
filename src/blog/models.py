from datetime import datetime

from django.db import models

# Create your models here.
from user_app.models import User

class Categorie(models.Model):
    libelle=models.CharField(max_length=100)
    desc=models.CharField(max_length=300)

    def __str__(self):
        return self.libelle

class Tag(models.Model):
    libelle=models.CharField(max_length=30)
    def __str__(self):
        return self.libelle

class Post(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    date=models.DateTimeField(auto_now_add=True)
    #image=models.ImageField(upload_to='post/images')
    titre=models.CharField(max_length=255)
    contenu=models.TextField()#MARKDOWN
    category=models.ForeignKey(Categorie,on_delete=models.SET_NULL,null=True)
    tags=models.ManyToManyField(Tag)
    is_valid=models.BooleanField(default=False)
    def __str__(self):
        return f"Post de {self.user} le {self.date.date()}"

class Comments(models.Model):
    post=models.ForeignKey(Post,on_delete=models.SET_NULL,null=True)
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    date=models.DateTimeField(auto_now_add=True)
    commentaire=models.CharField(max_length=1000)
    def __str__(self):
        return f"Commentaire de {self.user} au post de {self.post.user} le {self.date.date()}"

class Reponse(models.Model):
    commentaire_source=models.ForeignKey(Comments,on_delete=models.SET_NULL,null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    contenu=models.CharField(max_length=500)
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reponse de {self.user} au commentaire de {self.commentaire_source.user} le {self.date.date()} "




