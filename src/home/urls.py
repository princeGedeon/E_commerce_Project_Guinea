from django.urls import path

from home.views import index

from home.views import about

from home.views import contact

from authentication.views import get_profile

urlpatterns = [
    path('',index,name="index"),
    path('about-us/',about,name='about'),
    path('contact/',contact,name="contact"),
    path('profil/<str:slug>/',get_profile,name="get_profile")

]
