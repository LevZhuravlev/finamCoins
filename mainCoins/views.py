from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from .form import AuthUserForm, RegisterUserForm
from django.contrib.auth.models import User
from django.views.generic import CreateView
from django.contrib.auth import authenticate, login
from .models import Equities, FinCoins
from .coinLogic import coinPrice

# Create your views here.

def open(request):

    if request.user.is_authenticated:
        context = {}
        context['Equities'] = Equities.objects.order_by('price')
        try:
            context['Coins'] = FinCoins.objects.get(user_name=request.user)
        except:
            context['Coins'] = 0

        context['Differene'] = []
        context['Differene_proc'] = []
        coins = int(str(context['Coins']))
        for i in context['Equities']:
            i.price = round(coinPrice(i.price))
            context['Differene'].append(i.price-coins)
            context['Differene_proc'].append(str(round((coins/i.price)*100)) + '%')

        fusion = zip(context['Equities'], context['Differene'], context['Differene_proc'])
        return render(request, 'mainCoins/index.html', {'fusion': fusion, 'Coins': str(context['Coins'])})

    else:
        return redirect('/login')

def equitiess(request):

    if request.user.is_authenticated:
        context = {}
        context['Equities'] = Equities.objects.order_by('price')
        try:
            context['Coins'] = FinCoins.objects.get(user_name=request.user)
        except:
            context['Coins'] = 0

        context['Differene'] = []
        context['Differene_proc'] = []
        coins = int(str(context['Coins']))
        for i in context['Equities']:
            i.price = round(coinPrice(i.price))
            context['Differene'].append(i.price-coins)
            context['Differene_proc'].append(str(round((coins/i.price)*100)) + '%')

        fusion = zip(context['Equities'], context['Differene'], context['Differene_proc'])
        return render(request, 'mainCoins/allequitiess.html', {'fusion': fusion, 'Coins': str(context['Coins'])})

    else:
        return redirect('/login')




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
	next_page = '/login'