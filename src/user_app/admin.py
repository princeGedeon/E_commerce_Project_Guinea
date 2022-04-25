from django.contrib import admin

# Register your models here.
from user_app.models import User

from user_app.models import Member


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    class Meta:
        verbose_name="User"
    search_fields = ("username","email")
    list_display = ('username','email','nationalite','date_joined_')
    ordering = ["-date_joined",]
    list_filter = ("is_active",)

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    pass