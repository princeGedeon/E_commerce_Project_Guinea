from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView

from commerce.models import Product


class ProductListView(ListView):
    template_name = "pages/market/list_produits.html"
    paginate_by = 4  # add this
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['produits'] = Product.objects.all()
        return context

    def get_queryset(self):
        return Product.objects.all()

class ProductDetalView(DetailView):
    model = Product
    template_name = 'pages/market/detail_produit.html'
    object_name="produit"