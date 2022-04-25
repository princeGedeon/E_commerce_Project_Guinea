
from django.urls import path



from authentication.views import loginView

urlpatterns = [
    path('login/',loginView,name="login")

]
