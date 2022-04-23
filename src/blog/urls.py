from django.urls import path

from blog.views import blog_principal

urlpatterns = [
    path('',blog_principal,name="index")
]
