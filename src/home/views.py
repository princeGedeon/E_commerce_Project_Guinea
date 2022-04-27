from django.shortcuts import render

# Create your views here.
from user_app.models import Member

from blog.models import Post


def index(request):
    user=request.user

    l_post=Post.objects.all().order_by('-date')[0:4]
    context={"l_post":l_post,"user":user}
    return render(request,'pages/index.html',context)

def about(request):
    membres=Member.objects.all()
    context={'members':membres}
    return render(request,'pages/about.html',context)

def contact(request):
    return render(request,'pages/contact.html')