from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
# Create your views here.
from .forms import UserForm
from user_app.models import User


def loginView(request):
    if request.method=="POST":
        email=request.POST['email']
        password=request.POST['password']
        user=authenticate(request,email=email,password=password)
        if user is not None and user.is_active:
            login(request, user)
            if not user.is_valid:

                return redirect('profile_form')
            else:

                return redirect('index')
                print("Vous etes authentifié")


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

        else:
            messages.error(request, form.errors)
    return render(request,'pages/authentification/register.html',{'form':form})

@login_required(login_url='login')
def profileRegister(request):
    user=request.user

    if user.type=="VISITEUR":
        type=0
    elif user.type=="VENDEUR":
        type=1
    if request.method=="POST":
        if type==0:
            visiteur=user.visiteur
            user.bio=request.POST.get('bio')
            user.profile = request.FILES['profile']
            user.couverture = request.FILES['couverture']

            user.is_valid=True
            user.save()
            visiteur.save()
            return redirect('index')
        elif type==1:
            vendeur=user.vendeur
            vendeur.ville=request.POST.get('ville')
            user.bio=request.POST.get('bio')
            user.phone=request.POST.get('phone')
            vendeur.profession=request.POST.get('profession')
            user.nationalite=request.POST.get('nationalite')
            user.profile = request.FILES['profile']
            user.couverture = request.FILES['couverture']
            user.is_valid=True
            user.save()
            vendeur.save()


            return redirect('index')

    context={'user':user,'type':type}

    return render(request,"pages/authentification/profile_register.html",context)

@login_required(login_url='login')
def profile(request):

    context={"user":request.user}
    return render(request,"pages/profil.html")


def get_profile(request,slug):

    user=get_object_or_404(User,slug=slug)
    context={"user":user}
    return render(request,"pages/profilv2.html")

@login_required(login_url="login")
def deconnection(request):
    logout(request)
    return redirect("index")

