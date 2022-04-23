from django.contrib import admin

# Register your models here.
from blog.models import Comments,Reponse

admin.site.register(Comments)
admin.site.register(Reponse)