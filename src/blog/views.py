from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.views.generic import ListView, DetailView


from blog.models import Categorie,Tag,Post, Comments




class BlogListView(ListView):

    template_name = "pages/blog/blog.html"


    paginate_by = 4  # add this

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all()
        context['latest_posts']=context['posts'].order_by('-date')[0:4]
        context['categories']=Categorie.objects.all()

        return context



    def get_queryset(self):

        return Post.objects.all()

def BlogPostDetailView(request,slug):
    post=get_object_or_404(Post,slug=slug)
    template_name = 'pages/blog/blogpost.html'
    context ={'post':post}
    context['posts'] = Post.objects.all()
    context['latest_posts'] = context['posts'].order_by('-date')[0:4]
    context['categories'] = Categorie.objects.all()

    if request.user.is_authenticated:
        if request.method=='POST':
            r_post=request.POST.get('commentaire')
            r_comment=Comments.objects.create(commentaire=r_post,post=post,user=request.user)
            r_comment.save()
            return redirect('detail_post',slug=slug)

    return render(request,template_name,context)



