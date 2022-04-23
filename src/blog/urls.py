from django.urls import path

from blog.views import BlogListView,BlogPostDetailView


urlpatterns = [
    path('',BlogListView.as_view(),name="list_post"),
    path('blogpost/<str:slug>',BlogPostDetailView.as_view(),name="detail_post")
]
