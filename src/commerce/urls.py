from commerce.views import ProductListView, detailView

from django.urls import path

from commerce.views import reviewView

urlpatterns = [
    path('home/',ProductListView.as_view(template_name = "pages/market/list_produits.html"),name="list_produits"),
    path('home/v2',ProductListView.as_view(template_name = "pages/market/list_produits_v2.html"),name="list_produits_2"),
    path('article/<str:pk>',detailView,name="detail_produit"),
    path('review/<str:pk>',reviewView,name="review"),

]
