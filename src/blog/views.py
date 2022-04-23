from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView

from blog.models import Post


class BlogListView(ListView):

    template_name = "pages/blog/blog.html"
    context_object_name = "posts"

    paginate_by = 4  # add this

    def get_queryset(self):

        return Post.objects.all()

class BlogPostDetailView(DetailView):
    model = Post
    template_name = 'pages/blog/blogpost.html'
    context_object_name = 'post'

