from django.urls import path

from home.views import index

from home.views import about

from home.views import contact

urlpatterns = [
    path('',index,name="index"),
    path('about-us/',about,name='about'),
    path('contact/',contact,name="contact")

]
