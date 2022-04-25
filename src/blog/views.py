from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView


from blog.models import Categorie,Tag,Post


class BlogListView(ListView):

    template_name = "pages/blog/blog.html"


    paginate_by = 4  # add this

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all()
        context['latest_posts']=context['posts'].order_by('-date')[0:4]
        context['categories']=Categorie.objects.all()

        print(context)
        return context



    def get_queryset(self):

        return Post.objects.all()

class BlogPostDetailView(DetailView):
    model = Post
    template_name = 'pages/blog/blogpost.html'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all()
        context['latest_posts']=context['posts'].order_by('-date')[0:4]
        context['categories']=Categorie.objects.all()

        print(context)
        return context

