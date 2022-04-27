
from django.urls import path



from authentication.views import loginView,registerView,profileRegister,deconnection



urlpatterns = [

    path('login/',loginView,name="login"),
    path('logout/',deconnection,name='logout'),
    path('register/',registerView,name="register"),
    path("profil_add/",profileRegister,name="profile_form")

]
