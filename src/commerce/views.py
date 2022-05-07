from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView

from commerce.models import Product,Categorie



class ProductListView(ListView):

    context_product=Product.objects.all()
    queryset = Product.objects.all()





    def get_queryset(self):
        context_product = Product.objects.all()

        item = self.request.GET.get('recherche_article')
        sort=self.request.GET.get("sort")

        if item != '' and item is not None:
            context_product = Product.objects.filter(libelle__icontains=item)

        if sort != '' and sort is not None:
            if sort == 'rating':
                context_product = context_product.order_by('price')
            elif sort == 'rating2':
                context_product = context_product.order_by('-price')
            elif sort=='date':
                context_product=context_product.order_by("-date")

        page = self.request.GET.get('page', 1)
        paginator = Paginator(context_product, 12)
        try:
            context_product = paginator.page(page)
        except PageNotAnInteger:
            context_product = paginator.page(1)
        except EmptyPage:
            context_product= paginator.page(paginator.num_pages)
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