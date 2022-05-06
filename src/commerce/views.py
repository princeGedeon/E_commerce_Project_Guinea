from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView

from commerce.models import Product,Categorie



class ProductListView(ListView):

    context_product=Product.objects.all()
    template_name = "pages/market/list_produits.html"
    paginate_by = 16 # add this




    def get_queryset(self):
        item = self.request.GET.get('recherche_article')
        sort=self.request.GET.get("sort")

        if item != '' and item is not None:
            context_product = Product.objects.filter(libelle__icontains=item)

        else:
            context_product=Product.objects.all()

        if sort != '' and sort is not None:
            if sort == 'rating':
                context_product = context_product.order_by('price')
            elif sort == 'rating2':
                context_product = context_product.order_by('-price')
            elif sort=='date':
                context_product=context_product.order_by("-date")


        return context_product

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['produits'] =self.get_queryset()
        context['categories']=Categorie.objects.filter(is_visible=True)
        return context

class ProductDetalView(DetailView):
    model = Product
    template_name = 'pages/market/detail_produit.html'
    context_object_name="produit"