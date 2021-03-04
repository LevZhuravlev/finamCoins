from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def open(request):
    return render(request, 'mainCoins/index.html')