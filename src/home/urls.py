from django.urls import path

from home.views import index

from home.views import about

urlpatterns = [
    path('',index,name="index"),
    path('about-us/',about,name='about')

]
