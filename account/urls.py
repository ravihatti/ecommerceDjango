from django.urls import path
from account.views import login_page,register_page,activate_email
urlpatterns = [
    path('login/',login_page,name='login'),
    path('registration/',register_page,name='registration'),
    path('activate/<email_token>/',activate_email, name = "activate_email")
]