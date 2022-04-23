from django.contrib import admin

# Register your models here.
from blog.models import Comments,Reponse,Post, Tag, Categorie

from user_app.models import Achetteur,Vendeur


@admin.register(Comments)
class UserAdmin(admin.ModelAdmin):
    class Meta:
        verbose_name="Commentaires"

    ordering = ["-date",]
    list_filter = ("user",)



@admin.register(Achetteur)
class AchetteurAdmin(admin.ModelAdmin):
    class Meta:
        verbose_name="Achetteur"

@admin.register(Vendeur)
class VendeurAdmin(admin.ModelAdmin):
    class Meta:
        verbose_name="Vendeur"

admin.site.register(Post)
admin.site.register(Reponse)
admin.site.register(Tag)
admin.site.register(Categorie)
