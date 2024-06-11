from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView


class Login(LoginView):
    template_name = 'login.html'
    success_url = '/notes/'


class Register(CreateView):
    form_class = UserCreationForm
    template_name = 'register.html'
    success_url = '/notes/'


class Logout(LoginRequiredMixin, LogoutView):
    next_page = '/notes/'
    login_url = '/account/login/'
