from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
from .forms import UserForm


def loginView(request):
    if request.method=="POST":
        email=request.POST['email']
        password=request.POST['password']
        user=authenticate(request,email=email,password=password)
        if user is not None and user.is_active:
            login(request,user)
            messages.success(request,"Bienvenue")
            return redirect("index")
        else:
            messages.error(request,"Erreur d'authentification")

    return render(request,'pages/authentification/login.html')

def registerView(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Votre compte a été créé')
            return redirect('login')
        else:
            messages.error(request, form.errors)
    return render(request,'pages/authentification/register.html',{'form':form})




@login_required(login_url='login')
def deconnection(request):
    logout(request)
    return redirect("login")
