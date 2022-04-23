from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from blog.models import Post


class BlogListView(ListView):
    queryset = Post.objects.filter(is_valid=True)
    template_name = "pages/blog/blog.html"
    context_object_name = "posts"


