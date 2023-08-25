from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

# Create your views here.

class UserRegisterForm(generic.CreateView):
    form_class = UserCreationForm
    template_name = "registration/user_signup.html"
    success_url = reverse_lazy('login')
