from django.contrib import admin

# Register your models here.
from user_app.models import User

admin.site.register(User)

class UserAdmin(admin.ModelAdmin):
    class Meta:
        verbose_name="User"
    search_fields = ("username","email")
    list_display = ('username','email','nationalite',)
    ordering = ["-date",]
    list_filter = ("is_activate")