import requests
import datetime
from bs4 import BeautifulSoup
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from .form import *
from django.contrib.auth.models import User
from django.views.generic import View
from .models import Equities, StudentsInfo, TeachersInfo, Groups
from .coinLogic import coinPrice, get_current_coin_price




from django.utils import timezone

# d1 = d1 + datetime.timedelta(days=1)
# print(d1)

def foo():

    d1 = datetime.datetime.today()

    for equitie in Equities.objects.all():


        if equitie.date_of_last_update.day != d1.day:

            print(equitie, "стоимость", getPrice(equitie.company_url))
            equitie.price = getPrice(equitie.company_url)
            equitie.date_of_last_update = d1
            equitie.save()
        else:
            return
        
def getPrice(forCompanyWithUrl):
    URL = forCompanyWithUrl
    HEADERS = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36'}

    response = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(response.content, 'html.parser')
    item = soup.findAll('span', class_ = 'PriceInformation__price--26G')

    for i in item:
        res = i.get_text().rpartition(' ')[0]
        res = str(res)
        res = res.split(',')[0]
        res = ''.join(res.split())
        res = int(float(res))+1
    return res


