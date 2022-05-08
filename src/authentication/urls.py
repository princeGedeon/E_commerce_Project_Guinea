from django.contrib.auth import views
from django.urls import path



from authentication.views import loginView,registerView,profileRegister,deconnection



urlpatterns = [

    path('login/',loginView,name="login"),
    path('logout/',deconnection,name='logout'),
    path('register/',registerView,name="register"),
    path("profil_add/",profileRegister,name="profile_form"),
    path('reset_password', views.PasswordResetView.as_view(template_name="pages/authentification/password_reset.html"),name="reset_password"),
    path('reset_password_send', views.PasswordResetDoneView.as_view(template_name="pages/authentification/password_reset_sent.html"), name="password_reset_done"),
    path("reset/<uidb64>/<token>",views.PasswordResetConfirmView.as_view(template_name="pages/authentification/password_reset_form.html"),name="password_reset_confirm"),
    path('reset_password_complete',views.PasswordResetCompleteView.as_view(template_name="pages/authentification/password_reset_done.html"),name="password_reset_complete")

]
