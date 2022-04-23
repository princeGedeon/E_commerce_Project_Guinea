from django.contrib import admin

# Register your models here.
from blog.models import Comments,Reponse,Post, Tag, Categorie

@admin.register(Comments)
class UserAdmin(admin.ModelAdmin):
    class Meta:
        verbose_name="Commentaires"

    ordering = ["-date",]
    list_filter = ("user",)

admin.site.register(Post)
admin.site.register(Reponse)
admin.site.register(Tag)
admin.site.register(Categorie)