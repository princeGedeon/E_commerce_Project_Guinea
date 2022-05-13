from django.contrib import admin

# Register your models here.
from commerce.models import Product,Tags_Products,Stock,Categorie,Reviews


admin.site.register(Categorie)
admin.site.register(Tags_Products)
admin.site.register(Reviews)
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = ('libelle',"price","date","vendeur",)
    list_filter = ('vendeur',)
    ordering = ["-date",]


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):

    list_display = ('produit',"quantite","date","get_vendeur",)
    list_filter = ('quantite',)













    ()
