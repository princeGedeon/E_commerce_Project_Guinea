from django.shortcuts import render

# Create your views here.
from user_app.models import Member


def index(request):
    return render(request,'pages/index.html')

def about(request):
    membres=Member.objects.all()
    context={'members':membres}
    return render(request,'pages/about.html',context)