from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
# Create your views here.
from django.views.generic import ListView, DetailView

from commerce.models import Product,Categorie

from commerce.models import Reviews


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


def detailView(request,pk):
    produit=get_object_or_404(Product,pk=pk)
    template_name = 'pages/market/detail_produit.html'
    review=Reviews.objects.all()
    r=[(review[i],review[i+1]) for i in range(0,len(review)-1,2)]
    context={'produit':produit,"user":request.user,"reviews":r}
    return render(request,template_name,context)

def reviewView(request,pk):
    produit=get_object_or_404(Product,pk=pk)

    if request.user.is_authenticated:
        if request.method=='POST':
            title=request.POST.get('title')
            content=request.POST.get('content')
            note=request.POST.get('rating-input')
            review=Reviews.objects.create(title=title,note=note,content=content,user=request.user)

            review.save()
            return redirect('detail_produit',pk=produit.id)
    return render(request,"pages/market/reviews.html",{"produit":produit})