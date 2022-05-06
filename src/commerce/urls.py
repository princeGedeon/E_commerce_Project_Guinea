from commerce.views import ProductListView, ProductDetalView

from django.urls import path


urlpatterns = [
    path('home/',ProductListView.as_view(template_name = "pages/market/list_produits.html"),name="list_produits"),
    path('home/v2',ProductListView.as_view(template_name = "pages/market/list_produits_v2.html"),name="list_produits_2"),
    path('article/<str:pk>',ProductDetalView.as_view(),name="detail_produit")

]
