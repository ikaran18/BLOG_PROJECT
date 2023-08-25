from django.urls import path
from .views import *

urlpatterns = [
    path("usersignup/",UserRegisterForm.as_view(),name='user_signup'),
    
]
