from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from .form import AuthUserForm, RegisterUserForm
from django.contrib.auth.models import User


# Create your views here.

def open(request):
    return render(request, 'mainCoins/index.html')


class MyProjectLoginView(LoginView):
    template_name = 'mainCoins/login.html'
    form_class = AuthUserForm
    success_url = '/'

    def get_success_url(self):
        return self.success_url

from django.views.generic import CreateView

class RegisterUserView(CreateView):
    model = User
    template_name = 'mainCoins/registration.html'
    success_url ='/'
    success_msg = 'Пользователь создан'
    form_class = RegisterUserForm

class MyProjectLogout(LogoutView):
	next_page = '/'