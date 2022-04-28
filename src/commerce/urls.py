from commerce.views import ProductListView, ProductDetalView

from django.urls import path


urlpatterns = [
    path('home/',ProductListView.as_view(),name="list_produits"),
    path('article/<str:pk>',ProductDetalView.as_view(),name="detail_produit")

]
