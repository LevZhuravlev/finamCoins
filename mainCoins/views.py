from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from .form import AuthUserForm, RegisterUserForm
from django.contrib.auth.models import User
from django.views.generic import CreateView
from django.contrib.auth import authenticate, login

# Create your views here.

def open(request):
    return render(request, 'mainCoins/index.html')


class MyProjectLoginView(LoginView):
    template_name = 'mainCoins/login.html'
    form_class = AuthUserForm
    success_url = '/'

    def get_success_url(self):
        return self.success_url

class RegisterUserView(CreateView):
    model = User
    template_name = 'mainCoins/registration.html'
    success_url ='/'
    success_msg = 'Пользователь создан'
    form_class = RegisterUserForm

    def form_valid(self, form):
        form_valid = super().form_valid(form)
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        aut_user = authenticate(username=username, password=password)
        login(self.request, aut_user)
        return form_valid

class MyProjectLogout(LogoutView):
	next_page = '/'