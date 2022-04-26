from django.contrib.auth.forms import UserCreationForm

from user_app.models import User


class UserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','first_name','last_name','password1','password2']